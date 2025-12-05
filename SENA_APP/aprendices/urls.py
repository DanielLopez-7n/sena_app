from django.urls import path
from . import views

urlpatterns = [
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    path('aprendices/detalles/<int:aprendiz_id>/', views.details, name='details'),
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    
    # URL para agregar (Crear)
    path('aprendices/agregar/', views.crear_aprendiz, name='crear_aprendiz'), 
    
    # URL para editar (Actualizar)
    path('aprendices/editar/<int:aprendiz_id>/', views.editar_aprendiz, name='editar_aprendiz'),
    
    # URL para ver detalles (Leer)
    path('aprendices/detalles/<int:aprendiz_id>/', views.details, name='details'),
    
    #URL para eliminar (Eliminar)
    path('aprendices/<int:aprendiz_id>/eliminar/', views.eliminar_aprendiz, name='eliminar_aprendiz'),

]