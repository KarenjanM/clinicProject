from django.db import models
from base.models import Doctor, Patient


# Create your models here.
class Appointment(models.Model):
    date_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')


class Summary(models.Model):
    result = models.TextField()
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
