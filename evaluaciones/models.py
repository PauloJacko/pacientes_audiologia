from django.db import models
from Login.models import Paciente

class Evaluacion(models.Model):

    TIPO_CHOICES = [
        ('audiometria', 'Audiometría'),
        ('impedanciometria', 'Impedanciometría'),
        ('otoscopia', 'Otoscopía'),
        ('otro', 'Otro'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='evaluaciones')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)

    fecha = models.DateTimeField(auto_now_add=True)

    observaciones = models.TextField(blank=True)

    archivo = models.FileField(upload_to='evaluaciones/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.paciente.nombre} ({self.fecha.strftime('%d/%m/%Y')})"