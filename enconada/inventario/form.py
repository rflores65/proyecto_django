from django import forms
from .models import Arrendatario, Persona


class ArrendatarioForm(forms.ModelForm):
    class Meta:
        model  = Arrendatario
        fields = '__all__'

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'