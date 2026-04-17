from django.db import models

class Paciente(models.Model):

    PREVISION_CHOICES = [
        ('fonasa', 'Fonasa'),
        ('isapre', 'Isapre'),
        ('capredena', 'Capredena'),
        ('dipreca', 'Dipreca')
    ]

    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    prevision = models.CharField(
        max_length=20,
        choices=PREVISION_CHOICES,
        default='fonasa'
    )

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.rut}"