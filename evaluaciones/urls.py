from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    path('audiometria/<int:paciente_id>/', views.crear_audiometria, name='crear_audiometria'),
    path('impedanciometria/<int:paciente_id>/', views.crear_impedanciometria, name='crear_impedanciometria'),
    path('otoscopia/<int:paciente_id>/', views.crear_otoscopia, name='crear_otoscopia'),
    path('otro/<int:paciente_id>/', views.crear_evaluacion_otro, name='crear_evaluacion_otro'),
]