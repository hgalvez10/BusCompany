from django import forms

from apps.company.models import Driver, Bus


class driverForm(forms.ModelForm):
    class Meta:
        model = Driver
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


class busForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = [
            'driver',
            'license'
        ]
        label = {
            'driver': 'Chofer',
            'license': 'Patente',
        }
        widget = {
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'license': forms.TextInput(attrs={'class': 'form-control'}),
        }