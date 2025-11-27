from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz

def aprendices(request):
    mis_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'mis_aprendices': mis_aprendices,
    }
    return HttpResponse(template.render(context, request))