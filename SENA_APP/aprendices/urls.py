from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    path('aprendices/crear/', views.crear_aprendiz, name='crear_aprendiz'),
    path('aprendices/aprendiz/<int:aprendiz_id>/', views.details, name='detalle_aprendiz'),
    path('aprendices/<int:aprendiz_id>/editar/', views.editar_aprendiz, name='editar_aprendiz'),
    path('aprendices/<int:aprendiz_id>/eliminar/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
]