from django.shortcuts import render
from .models import Programa
from .forms import ProgramaForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# 1. READ (Lista)
def lista_programas(request):
    programas = Programa.objects.all()
    context = {'programas': programas}
    return render(request, 'lista_programas.html', context)

# 2. READ (Detalle)
def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id) 
    context = {'programa': programa}
    return render(request, 'details_programa.html', context)

# 3. CREATE
def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_programas') 
    else:
        form = ProgramaForm()
        
    context = {'form': form, 'titulo': 'Crear Nuevo Programa', 'es_edicion': False}
    return render(request, 'programa_form.html', context)

# 4. UPDATE
def editar_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id) 
    
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('detalle_programa', programa_id=programa.id) 
    else:
        form = ProgramaForm(instance=programa)
        
    context = {'form': form, 'titulo': f'Editar Programa: {programa.nombre}', 'programa': programa, 'es_edicion': True}
    return render(request, 'programa_form.html', context)