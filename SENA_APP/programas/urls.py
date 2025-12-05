# programas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # READ (Lista)
    path('', views.lista_programas, name='lista_programas'),
    
    # CREATE
    path('agregar/', views.crear_programa, name='crear_programa'), 
    
    # UPDATE
    path('editar/<int:programa_id>/', views.editar_programa, name='editar_programa'),
    
    # READ (Detalle)
    path('detalles/<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
    
    # DELETE
    path('programas/<int:programa_id>/eliminar/', views.eliminar_programa, name='eliminar_programa'),

]