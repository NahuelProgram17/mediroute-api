from rest_framework import viewsets, filters
from .models import Trip
from .serializers import TripSerializer


class TripViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar viajes de transporte médico.
    Soporta: listar, crear, ver, editar y eliminar viajes.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['patient_name', 'status', 'pickup_address']
    ordering_fields = ['scheduled_time', 'created_at', 'status']