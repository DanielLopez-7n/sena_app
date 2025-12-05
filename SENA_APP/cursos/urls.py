# curso/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # READ (Lista) - Alias: lista_cursos
    path('', views.lista_cursos, name='lista_cursos'),
    
    # CREATE - Alias: crear_curso
    path('agregar/', views.crear_curso, name='crear_curso'), 
    
    # UPDATE - Alias: editar_curso
    path('editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    
    # READ (Detalle) - Alias: detalle_curso
    path('detalles/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]