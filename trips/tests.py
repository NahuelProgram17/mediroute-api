import pytest
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Trip


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(db):
    user = User.objects.create_user(
        username='testuser',
        password='testpass123'
    )
    client = APIClient()
    response = client.post('/api/auth/token/', {
        'username': 'testuser',
        'password': 'testpass123'
    })
    token = response.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client


@pytest.fixture
def sample_trip(db):
    return Trip.objects.create(
        patient_name='Juan Perez',
        pickup_address='Av. Corrientes 1234, CABA',
        dropoff_address='Hospital Italiano, CABA',
        scheduled_time=timezone.now(),
        status='pending'
    )


@pytest.mark.django_db
def test_create_trip(authenticated_client):
    data = {
        'patient_name': 'Maria Garcia',
        'pickup_address': 'Av. Santa Fe 567, CABA',
        'dropoff_address': 'Hospital Rivadavia, CABA',
        'scheduled_time': timezone.now().isoformat(),
        'status': 'pending'
    }
    response = authenticated_client.post('/api/trips/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['patient_name'] == 'Maria Garcia'


@pytest.mark.django_db
def test_list_trips(authenticated_client, sample_trip):
    response = authenticated_client.get('/api/trips/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_trip(authenticated_client, sample_trip):
    response = authenticated_client.get(f'/api/trips/{sample_trip.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['patient_name'] == 'Juan Perez'


@pytest.mark.django_db
def test_update_trip_status(authenticated_client, sample_trip):
    response = authenticated_client.patch(
        f'/api/trips/{sample_trip.id}/',
        {'status': 'in_progress'},
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data['status'] == 'in_progress'


@pytest.mark.django_db
def test_delete_trip(authenticated_client, sample_trip):
    response = authenticated_client.delete(f'/api/trips/{sample_trip.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_unauthenticated_access(api_client):
    response = api_client.get('/api/trips/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED