# instructores/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Instructor
from .forms import InstructorForm

# 1. READ (Lista)
def instructores(request):
    mis_instructores = Instructor.objects.all() # Retorna objetos, no solo values()
    context = {
        'mis_instructores': mis_instructores,
    }
    return render(request, 'lista_instructores.html', context)

# 2. READ (Detalle)
def details_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id) 
    context = {'instructor': instructor}
    return render(request, 'details_instructor.html', context)

# 3. CREATE
def crear_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_instructores') 
    else:
        form = InstructorForm()
        
    context = {'form': form, 'titulo': 'Agregar Nuevo Instructor', 'es_edicion': False}
    return render(request, 'instructor_form.html', context)

# 4. UPDATE
def editar_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id) 
    
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('details_instructor', instructor_id=instructor.id) 
    else:
        form = InstructorForm(instance=instructor)
        
    context = {'form': form, 'titulo': f'Editar Instructor: {instructor.nombre}', 'instructor': instructor, 'es_edicion': True}
    return render(request, 'instructor_form.html', context)




# Hasta el momento no se implementa la funcionalidad de eliminar instructores.
# def eliminar_instructor(request, instructor_id):
#     instructor = get_object_or_404(Instructor, id=instructor_id)
#     if request.method == 'POST':
#         instructor.delete()
#         return redirect('lista_instructores')
#     return render(request, 'confirm_delete_instructor.html', {'instructor': instructor})