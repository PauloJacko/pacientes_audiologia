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
    
from django.db import models

class Anamnesis(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='anamnesis')

    fecha = models.DateTimeField(auto_now_add=True)

    motivo_consulta = models.TextField()

    antecedentes_medicos = models.TextField(blank=True, null=True)
    antecedentes_auditivos = models.TextField(blank=True, null=True)

    hipoacusia = models.BooleanField(default=False)
    tinnitus = models.BooleanField(default=False)
    vertigo = models.BooleanField(default=False)
    otalgia = models.BooleanField(default=False)

    exposicion_ruido = models.BooleanField(default=False)
    uso_audifonos = models.BooleanField(default=False)

    medicamentos = models.TextField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Anamnesis {self.paciente.nombre} - {self.fecha.strftime('%d/%m/%Y')}"