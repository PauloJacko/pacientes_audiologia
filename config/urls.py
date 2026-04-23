from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Login.urls')),
    path('evaluaciones/', include('evaluaciones.urls')),
]