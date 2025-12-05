# curso/forms.py
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'codigo', 'nombre', 'programa', 'instructor_coordinador', 
            'fecha_inicio', 'fecha_fin', 'horario', 'aula', 
            'cupos_maximos', 'estado', 'observaciones'
        ]
        
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            # Las ForeignKeys se renderizan como Select por defecto, pero aplicamos la clase
            'programa': forms.Select(attrs={'class': 'form-select'}),
            'instructor_coordinador': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'aula': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos_maximos': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
