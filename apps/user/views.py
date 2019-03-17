from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.user.form import registryForm

# Create your views here.
class registryUser(CreateView):
    model = User
    template_name = "user/registry.html"
    form_class = registryForm
    success_url = reverse_lazy('sales:viewJourneys')

