from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

#from . import views
#from django.conf.urls import url, include
from apps.company.views import *

app_name = 'company'
urlpatterns = [
    path('indexDriver', login_required(indexDriver), name='indexDriver'),
    path('createDriver', login_required(createDriver), name='createDriver'),
    re_path(r'^editDriver/(?P<id_driver>\d+)/$', login_required(editDriver), name='editDriver'),
    re_path(r'^deleteDriver/(?P<id_driver>\d+)/$', login_required(deleteDriver), name='deleteDriver'),
    path('indexBus', login_required(indexBus), name='indexBus'),
    path('createBus', login_required(createBus), name='createBus'),
    re_path(r'^editBus/(?P<id_bus>\d+)/$', login_required(editBus), name='editBus'),
    re_path(r'^deleteBus/(?P<id_bus>\d+)/$', login_required(deleteBus), name='deleteBus'),
]


