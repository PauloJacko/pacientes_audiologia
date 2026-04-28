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

class Audiometria(models.Model):

    evaluacion = models.OneToOneField(
        'Evaluacion',
        on_delete=models.CASCADE,
        related_name="audiometria"
    )

    # CONFIG
    modo = models.CharField(max_length=20, default="tonal")

    # AUDIOGRAMA
    audiograma = models.JSONField(default=list, blank=True)

    # LOGOAUDIOMETRÍA
    sds_od = models.IntegerField(null=True, blank=True)
    sds_oi = models.IntegerField(null=True, blank=True)
    int_od = models.IntegerField(null=True, blank=True)
    int_oi = models.IntegerField(null=True, blank=True)
    mkg_od = models.IntegerField(null=True, blank=True)
    mkg_oi = models.IntegerField(null=True, blank=True)

    # PTP
    ptp_va_od = models.IntegerField(null=True, blank=True)
    ptp_vo_od = models.IntegerField(null=True, blank=True)
    ptp_va_oi = models.IntegerField(null=True, blank=True)
    ptp_vo_oi = models.IntegerField(null=True, blank=True)

    # ACUMETRÍA
    weber_250 = models.CharField(max_length=10, blank=True)
    weber_500 = models.CharField(max_length=10, blank=True)
    weber_1000 = models.CharField(max_length=10, blank=True)

    rinne_512_od = models.CharField(max_length=5, blank=True)
    rinne_512_oi = models.CharField(max_length=5, blank=True)

    # DETERIORO
    deterioro_test = models.CharField(max_length=20, blank=True)

    det_500_od = models.IntegerField(null=True, blank=True)
    det_1000_od = models.IntegerField(null=True, blank=True)
    det_2000_od = models.IntegerField(null=True, blank=True)
    det_4000_od = models.IntegerField(null=True, blank=True)

    det_500_oi = models.IntegerField(null=True, blank=True)
    det_1000_oi = models.IntegerField(null=True, blank=True)
    det_2000_oi = models.IntegerField(null=True, blank=True)
    det_4000_oi = models.IntegerField(null=True, blank=True)

    # TINNITUS
    tin_presente = models.BooleanField(default=False)
    tin_ausente = models.BooleanField(default=False)
    tin_ocasional = models.BooleanField(default=False)
    tin_examen_positivo = models.BooleanField(default=False)

    tin_od = models.BooleanField(default=False)
    tin_oi = models.BooleanField(default=False)
    tin_bilateral = models.BooleanField(default=False)

    tin_tono_puro = models.BooleanField(default=False)
    tin_ruido_blanco = models.BooleanField(default=False)
    tin_ruido_banda = models.BooleanField(default=False)

    tin_continuo = models.BooleanField(default=False)
    tin_pulsatil = models.BooleanField(default=False)
    tin_fluctuante = models.BooleanField(default=False)

    tin_db_hl = models.IntegerField(null=True, blank=True)
    tin_db_sl = models.IntegerField(null=True, blank=True)
    tin_freq = models.IntegerField(null=True, blank=True)
    tin_masking = models.IntegerField(null=True, blank=True)

    tin_inh_od = models.BooleanField(default=False)
    tin_inh_oi = models.BooleanField(default=False)
    tin_inh_bi = models.BooleanField(default=False)
    tin_inh_tc = models.BooleanField(default=False)

    def __str__(self):
        return f"Audiometría - {self.evaluacion.paciente.nombre}"