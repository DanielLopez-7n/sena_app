# curso/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
# Importaciones relativas: usa el punto (.) para referenciar modelos y formularios
from .models import Curso
from .forms import CursoForm
# Nota: get_object_or_404, render, y redirect son importados arriba.

# 1. READ (Lista de Cursos)
def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'lista_cursos.html', context)

# 2. READ (Detalle de un Curso)
def detalle_curso(request, curso_id):
    # Obtiene el curso junto con su programa e instructor coordinador (select_related)
    curso = get_object_or_404(
        Curso.objects.select_related('programa', 'instructor_coordinador'), 
        id=curso_id
    )

    # Obtiene las relaciones ManyToMany (Instructores y Aprendices)
    # Estos objetos se usan en detalle_curso.html
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    return render(request, 'detalle_curso.html', context)

# 3. CREATE (Crear Curso)
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos') 
    else:
        form = CursoForm()
        
    context = {'form': form, 'titulo': 'Crear Nuevo Curso', 'es_edicion': False}
    return render(request, 'curso_form.html', context)

# 4. UPDATE (Editar Curso)
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id) 
    
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('detalle_curso', curso_id=curso.id) 
    else:
        form = CursoForm(instance=curso)
        
    context = {'form': form, 'titulo': f'Editar Curso: {curso.codigo} - {curso.nombre}', 'curso': curso, 'es_edicion': True}
    return render(request, 'curso_form.html', context)

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')

    return render(request, 'confirm_delete_curso.html', {'curso': curso})

