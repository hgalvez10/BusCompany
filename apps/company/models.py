from django.db import models

# Create your models here.


class Driver(models.Model):
    rut = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class Bus(models.Model):
    driver = models.ForeignKey(Driver, null=True, blank=True, default=None, on_delete=models.PROTECT)
    license = models.CharField(max_length=6)

    def __str__(self):
        return '{}'.format(self.license)
