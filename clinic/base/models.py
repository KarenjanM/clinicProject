from django.db import models


class Room(models.Model):
    number = models.IntegerField()


# Create your models here.
class BaseUser(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=20, blank=False)

    class Meta:
        abstract = True


class Doctor(BaseUser):
    room = models.OneToOneField(Room, on_delete=models.SET_NULL)
    is_working = models.BooleanField(default=True)


class Patient(BaseUser):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, related_name='patients')
