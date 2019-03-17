from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.company.models import Bus


class Schedule(models.Model):
    hour = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.hour)


class Journey(models.Model):
    states = (
        ('0', 'Inactivo'),
        ('1', 'Activo'),
    )
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    schedule = models.ForeignKey(Schedule, null=True, blank=True, default=None, on_delete=models.PROTECT)
    date = models.DateField()
    state = models.CharField(max_length=20, default=1, choices=states)

    def __str__(self):
        return '{}-{}'.format(self.origin, self.destination)


class Passenger(models.Model):
    rut = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class Trip(models.Model):
    bus = models.ForeignKey(Bus, null=True, blank=True, default=None, on_delete=models.DO_NOTHING)
    journey = models.ForeignKey(Journey, null=True, blank=True, default=None, on_delete=models.DO_NOTHING)


class Ticket(models.Model):
    seats = (
        ('1', 'N° 1'),
        ('2', 'N° 2'),
        ('3', 'N° 3'),
        ('4', 'N° 4'),
        ('5', 'N° 5'),
        ('6', 'N° 6'),
        ('7', 'N° 7'),
        ('8', 'N° 8'),
        ('9', 'N° 9'),
        ('10', 'N° 10')
    )
    numSeat = models.CharField(max_length=20, default=1, choices=seats)
    trip = models.ForeignKey(Trip, null=True, blank=True, default=None, on_delete=models.PROTECT)
    passenger = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return '{}-{}: {}'.format(self.numSeat, self.trip, self.passenger)
