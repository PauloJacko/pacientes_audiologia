from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    # CREAR EVALUACIONES
    path('audiometria/crear/<int:paciente_id>/', views.crear_audiometria, name='crear_audiometria'),
    path('impedanciometria/crear/<int:paciente_id>/', views.crear_impedanciometria, name='crear_impedanciometria'),
    path('otoscopia/crear/<int:paciente_id>/', views.crear_otoscopia, name='crear_otoscopia'),
    path('otro/crear/<int:paciente_id>/', views.crear_evaluacion_otro, name='crear_evaluacion_otro'),

    # VER / EDITAR / ELIMINAR EVALUACIONES
    path('audiometria/<int:id>/', views.ver_audiometria, name='ver_audiometria'),
    path('audiometria/<int:id>/editar/', views.editar_audiometria, name='editar_audiometria'),
    path('evaluacion/<int:id>/eliminar/', views.eliminar_evaluacion, name='eliminar_evaluacion'),
    path('audiometria/<int:id>/pdf/', views.ver_audiometria_pdf, name='ver_audiometria_pdf'),
    path('otoscopia/<int:id>/ver/', views.ver_otoscopia, name='ver_otoscopia'),
    path('otoscopia/<int:id>/editar/', views.editar_otoscopia, name='editar_otoscopia'),
    path('impedanciometria/<int:id>/ver/', views.ver_impedanciometria, name='ver_impedanciometria'),
    path('impedanciometria/<int:id>/editar/', views.editar_impedanciometria, name='editar_impedanciometria'),
]