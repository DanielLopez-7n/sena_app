from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['documento_identidad', 'nombre', 'apellido', 'telefono', 'correo', 'fecha_nacimiento', 'ciudad', 'programa']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean_documento_identidad(self):
        documento = self.cleaned_data.get('documento_identidad')
        if not documento.isdigit():
            raise forms.ValidationError('El documento solo admite solo numeros.')
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:  # es opcional, solo validar si fue ingresado
            if not telefono.isdigit():
                raise forms.ValidationError('El teléfono solo debe contener números.')
            if len(telefono) != 10:
                raise forms.ValidationError('El teléfono debe tener exactamente 10 dígitos.')
        return telefono