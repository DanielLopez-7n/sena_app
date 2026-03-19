from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import Aprendiz
from .forms import AprendizForm

def aprendices(request):
    mis_aprendices = Aprendiz.objects.all()
    template = loader.get_template('lista_aprendices.html')
    context = {'mis_aprendices': mis_aprendices}
    return HttpResponse(template.render(context, request))

def details(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    context = {'aprendiz': aprendiz}
    template = loader.get_template('details.html')
    return HttpResponse(template.render(context, request))

def crear_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aprendices:lista_aprendices')
    else:
        form = AprendizForm()
    context = {'form': form, 'titulo': 'Agregar Nuevo Aprendiz', 'es_edicion': False}
    return render(request, 'aprendiz_form.html', context)

def editar_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=aprendiz)
        if form.is_valid():
            form.save()
            return redirect('aprendices:detalle_aprendiz', aprendiz_id=aprendiz.id)
    else:
        form = AprendizForm(instance=aprendiz)
    context = {'form': form, 'titulo': f'Editar Aprendiz: {aprendiz.nombre}', 'aprendiz': aprendiz, 'es_edicion': True}
    return render(request, 'aprendiz_form.html', context)

def home_page(request):
    return render(request, 'main.html')

def eliminar_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        aprendiz.delete()
        return redirect('aprendices:lista_aprendices')
    return render(request, 'confirm_delete_aprendiz.html', {'aprendiz': aprendiz})