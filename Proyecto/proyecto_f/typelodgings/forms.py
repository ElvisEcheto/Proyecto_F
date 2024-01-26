from django import forms
from . models import Typelodging

class TypelodgingForm(forms.ModelForm):
    class Meta:
        model = Typelodging
        fields = "__all__"
        exclude = ['status']
        labels = {
            'image': 'Imagen',
            'name': 'Nombre',                 
        }
        widgets = {
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el documento'}),        
        }