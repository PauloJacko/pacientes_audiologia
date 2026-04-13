from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.rut}"