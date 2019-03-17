from django.contrib import admin

from apps.sales.models import Passenger, Schedule, Journey, Trip, Ticket

# Register your models here.

admin.site.register(Passenger)
admin.site.register(Schedule)
admin.site.register(Journey)
admin.site.register(Trip)
admin.site.register(Ticket)
