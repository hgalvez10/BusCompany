from django.urls import path
from apps.user.views import *

app_name = 'user'
urlpatterns = [
    path('registryUser', registryUser.as_view(), name='registryUser'),
]