from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect #Añade 'render' y 'redirect'
from .models import Aprendiz
from .forms import AprendizForm
# Tu función existente para la lista (se mantiene)
def aprendices(request):
    mis_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'mis_aprendices': mis_aprendices,
    }
    return HttpResponse(template.render(context, request))

def details(request, aprendiz_id): 
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id) 
    
    context = {
        'aprendiz': aprendiz, 
    }
    
    template = loader.get_template('details.html')
    return HttpResponse(template.render(context, request))

# 1. FUNCIÓN PARA CREAR UN NUEVO APRENDIZ (C del CRUD)
def crear_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aprendices') 
    else:
        form = AprendizForm() 
        
    context = {'form': form, 'titulo': 'Agregar Nuevo Aprendiz', 'es_edicion': False}
    return render(request, 'aprendiz_form.html', context)


# 2. FUNCIÓN PARA EDITAR UN APRENDIZ EXISTENTE (U del CRUD)
def editar_aprendiz(request, aprendiz_id):
    # Obtiene el aprendiz a editar o devuelve 404
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id) 
    
    if request.method == 'POST':
        # Pasa los nuevos datos (request.POST) y la instancia del objeto (aprendiz)
        form = AprendizForm(request.POST, instance=aprendiz)
        if form.is_valid():
            form.save()
            # Redirige a la vista de detalles del aprendiz editado
            return redirect('details', aprendiz_id=aprendiz.id) 
    else:
        # Muestra el formulario precargado con los datos del aprendiz (GET)
        form = AprendizForm(instance=aprendiz)
        
    context = {'form': form, 'titulo': f'Editar Aprendiz: {aprendiz.nombre}', 'aprendiz': aprendiz, 'es_edicion': True}
    return render(request, 'aprendiz_form.html', context)

def home_page(request):
    # Asegúrate de que este archivo pueda acceder a 'main.html'
    return render(request, 'main.html')

def eliminar_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)

    if request.method == 'POST':
        aprendiz.delete()
        return redirect('lista_aprendices')

    return render(request, 'confirm_delete_aprendiz.html', {'aprendiz': aprendiz})

