# instructores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1. READ (Lista) - Ruta principal del módulo: /instructores/
    path('', views.instructores, name='lista_instructores'),
    
    # 2. CREATE - Ruta para el formulario de agregar: /instructores/agregar/
    path('agregar/', views.crear_instructor, name='crear_instructor'), 
    
    # 3. UPDATE - Ruta para el formulario de edición: /instructores/editar/5/
    path('editar/<int:instructor_id>/', views.editar_instructor, name='editar_instructor'),
    
    # 4. READ (Detalle) - Ruta para ver un instructor específico: /instructores/detalles/5/
    path('detalles/<int:instructor_id>/', views.details_instructor, name='details_instructor'),
    path('eliminar/<int:instructor_id>/', views.eliminar_instructor, name='eliminar_instructor'),
]
