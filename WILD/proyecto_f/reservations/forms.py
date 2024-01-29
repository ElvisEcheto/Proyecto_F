from django import forms
from . models import Reservation

from rstatus.models import Rstatu
from costumers.models import Costumer

class ReservationForm(forms.ModelForm):
    Rstatu = forms.ModelChoiceField(queryset=Rstatu.objects.filter(status=True).order_by('name'))
    Costumer = forms.ModelChoiceField(queryset=Costumer.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Reservation
        fields = "__all__"
        exclude = ['status']
        labels = {
            'daterr': 'Fecha de Reserva',
            'datess': 'Fecha comienzo',
            'dateff': 'Fecha fin',
            'value': 'Valor',
            'costumer' : 'Cliente',
            'rstatu' : 'Estado Reserva',     
        }
        widgets = {
            'daterr': forms.DateInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'datess': forms.DateInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'dateff': forms.DateInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
        }