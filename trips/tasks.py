from celery import shared_task
from django.utils import timezone


@shared_task
def send_trip_reminder(trip_id, patient_name, scheduled_time):
    """
    Tarea asíncrona que simula el envío de un recordatorio
    de viaje médico al paciente.
    """
    print(f"[{timezone.now()}] Enviando recordatorio a {patient_name}")
    print(f"Su viaje #{trip_id} está programado para {scheduled_time}")
    return f"Recordatorio enviado para viaje #{trip_id}"