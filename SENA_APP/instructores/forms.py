# instructores/forms.py
from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        # 📌 CAMPOS ACTUALIZADOS SEGÚN TU MODELO
        fields = [
            'tipo_documento', 
            'documento_identidad', 
            'nombre', 
            'apellido', 
            'telefono', 
            'correo', 
            'fecha_nacimiento', 
            'ciudad', 
            'direccion', 
            'nivel_educativo', 
            'especialidad', 
            'anos_experiencia', 
            'activo', 
            'fecha_vinculacion'
        ]
        
        # 📌 WIDGETS para aplicar clases de Bootstrap y tipos de input específicos
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_educativo': forms.Select(attrs={'class': 'form-select'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'anos_experiencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_vinculacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # El campo 'activo' (BooleanField) se renderiza como checkbox por defecto, no necesita widget.
        }