from django import forms
from django.forms import SelectDateWidget

from apps.sales.models import Passenger, Journey, Trip, Ticket


class passengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
                 'name',
                 'rut'
        ]
        label = {
                'name': 'Nombre',
                'rut': 'Rut',
        }
        widget = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'rut': forms.TextInput(attrs={'class': 'form-control'}),
        }


class journeyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = [
            'origin',
            'destination',
            'date',
            'schedule',
            'state'
        ]
        label = {
            'origin': 'Origen',
            'destination': 'Destino',
            'date': 'Fecha',
            'schedule': 'Hora',
            'state': 'Estado',
        }
        widget = {
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),
            'schedule': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }


class addBusForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'bus',
            'journey'
        ]
        label = {
            'bus': 'BusAsignado',
            'journey': 'Trayecto',
        }
        widget = {
            'bus': forms.Select(attrs={'class': 'form-control'}),
            'journey': forms.HiddenInput(attrs={'type': 'hidden'}),
        }


class buyTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'numSeat',
            'trip',
            'passenger'
        ]
        label = {
            'numSeat': 'BusAsignado',
            'trip': 'Trayecto',
            'passenger': 'Pasajero',
        }
        widget = {
            'numSeat': forms.Select(attrs={'class': 'form-control'}),
            'trip': forms.HiddenInput(attrs={'type': 'hidden'}),
            'passenger': forms.HiddenInput(attrs={'type': 'hidden'}),
        }
