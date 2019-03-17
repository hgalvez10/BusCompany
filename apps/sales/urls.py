from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from apps.sales.views import *

app_name = 'sales'
urlpatterns = [
    path('viewMyRedirect', login_required(viewMyRedirect), name='viewMyRedirect'),
    path('indexPassenger', login_required(indexPassenger), name='indexPassenger'),
    path('createPassenger', login_required(createPassenger), name='createPassenger'),
    re_path(r'^editPassenger/(?P<id_passenger>\d+)/$', login_required(editPassenger), name='editPassenger'),
    re_path(r'^deletePassenger/(?P<id_passenger>\d+)/$', login_required(deletePassenger), name='deletePassenger'),
    path('indexJourney', login_required(indexJourney), name='indexJourney'),
    path('averageJourney', login_required(averageJourney), name='averageJourney'),
    path('createJourney', login_required(createJourney), name='createJourney'),
    re_path(r'^editJourney/(?P<id_journey>\d+)/$', login_required(editJourney), name='editJourney'),
    re_path(r'^deleteJourney/(?P<id_journey>\d+)/$', login_required(deleteJourney), name='deleteJourney'),
    re_path(r'^addBusJourney/(?P<id_journey>\d+)/$', login_required(addBusJourney), name='addBusJourney'),
    path('viewJourneys', login_required(viewJourneys), name='viewJourneys'),
    re_path(r'^buyTicket/(?P<id_trip>\d+)/$', login_required(buyTicket), name='buyTicket'),
    path('indexTicket', login_required(indexTicket), name='indexTicket'),
    path('porcentageCapacity', login_required(porcentageCapacity), name='porcentageCapacity'),
]