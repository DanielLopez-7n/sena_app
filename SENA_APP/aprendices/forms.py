from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    # Clase Meta que vincula el formulario con el modelo y los campos de la BD
    class Meta:
        model = Aprendiz
        fields = ['documento_identidad', 'nombre', 'apellido', 'telefono', 'correo', 'fecha_nacimiento', 'ciudad', 'programa']
        # Opcional: Puedes añadir widgets para mejorar la apariencia (ej. selectores de fecha)
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }