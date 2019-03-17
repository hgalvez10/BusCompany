from django.contrib import admin

from apps.company.models import Bus
from apps.company.models import Driver
# Register your models here.
admin.site.register(Bus)
admin.site.register(Driver)
