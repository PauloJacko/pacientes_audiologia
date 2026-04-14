from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('crear-paciente/', views.crear_paciente, name='crear_paciente'),
    path('eliminar_paciente/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('paciente/<int:id>/', views.ver_paciente, name='ver_paciente'),
]