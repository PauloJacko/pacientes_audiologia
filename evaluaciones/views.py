from django.shortcuts import render, redirect, get_object_or_404
from Login.models import Paciente
from .models import Evaluacion, Audiometria, Otoscopia
from Login.models import Paciente
import json


def crear_audiometria(request, paciente_id):

    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":

        # 🔊 AUDIOGRAMA (JSON)
        audiograma_json = request.POST.get("audiograma_json")
        try:
            audiograma = json.loads(audiograma_json) if audiograma_json else []
        except:
            audiograma = []

        # 🧾 CREAR EVALUACION (contenedor)
        evaluacion = Evaluacion.objects.create(
            paciente=paciente,
            tipo="audiometria",
            observaciones=request.POST.get("observaciones", ""),
            archivo=request.FILES.get("archivo")
        )

        # 🧠 CREAR AUDIOMETRIA (detalle clínico)
        Audiometria.objects.create(

            evaluacion=evaluacion,

            # CONFIG
            modo=request.POST.get("tipo", "tonal"),

            # AUDIOGRAMA
            audiograma=audiograma,

            # LOGOAUDIOMETRÍA
            sds_od=request.POST.get("sds_od") or None,
            sds_oi=request.POST.get("sds_oi") or None,
            int_od=request.POST.get("int_od") or None,
            int_oi=request.POST.get("int_oi") or None,
            mkg_od=request.POST.get("mkg_od") or None,
            mkg_oi=request.POST.get("mkg_oi") or None,

            # PTP
            ptp_va_od=request.POST.get("ptp_va_od") or None,
            ptp_vo_od=request.POST.get("ptp_vo_od") or None,
            ptp_va_oi=request.POST.get("ptp_va_oi") or None,
            ptp_vo_oi=request.POST.get("ptp_vo_oi") or None,

            # ACUMETRÍA
            weber_250=request.POST.get("weber_250", ""),
            weber_500=request.POST.get("weber_500", ""),
            weber_1000=request.POST.get("weber_1000", ""),

            rinne_512_od=request.POST.get("rinne_512_od", ""),
            rinne_512_oi=request.POST.get("rinne_512_oi", ""),

            # DETERIORO
            deterioro_test=request.POST.get("deterioro_test", ""),

            det_500_od=request.POST.get("det_500_od") or None,
            det_1000_od=request.POST.get("det_1000_od") or None,
            det_2000_od=request.POST.get("det_2000_od") or None,
            det_4000_od=request.POST.get("det_4000_od") or None,

            det_500_oi=request.POST.get("det_500_oi") or None,
            det_1000_oi=request.POST.get("det_1000_oi") or None,
            det_2000_oi=request.POST.get("det_2000_oi") or None,
            det_4000_oi=request.POST.get("det_4000_oi") or None,

            # TINNITUS (checkbox = True si existe en POST)
            tin_presente="tin_presente" in request.POST,
            tin_ausente="tin_ausente" in request.POST,
            tin_ocasional="tin_ocasional" in request.POST,
            tin_examen_positivo="tin_examen" in request.POST,

            tin_od="tin_od" in request.POST,
            tin_oi="tin_oi" in request.POST,
            tin_bilateral="tin_bilateral" in request.POST,

            tin_tono_puro="tin_tono" in request.POST,
            tin_ruido_blanco="tin_ruido_blanco" in request.POST,
            tin_ruido_banda="tin_ruido_banda" in request.POST,

            tin_continuo="tin_continuo" in request.POST,
            tin_pulsatil="tin_pulsatil" in request.POST,
            tin_fluctuante="tin_fluctuante" in request.POST,

            tin_db_hl=request.POST.get("tin_db_hl") or None,
            tin_db_sl=request.POST.get("tin_db_sl") or None,
            tin_freq=request.POST.get("tin_freq") or None,
            tin_masking=request.POST.get("tin_masking") or None,

            tin_inh_od="tin_inh_od" in request.POST,
            tin_inh_oi="tin_inh_oi" in request.POST,
            tin_inh_bi="tin_inh_bi" in request.POST,
            tin_inh_tc="tin_inh_tc" in request.POST,
        )

        # 🔁 REDIRECCIÓN
        return redirect("ver_paciente", paciente.id)

    # GET
    return render(request, "evaluaciones/audiometria_form.html", {
        "paciente": paciente
    })


def ver_audiometria(request, id):
    evaluacion = get_object_or_404(Evaluacion, id=id)

    return render(request, 'evaluaciones/ver_audiometria.html', {
        'evaluacion': evaluacion,
        'audiometria': evaluacion.audiometria
    })

def ver_audiometria_pdf(request, id):
    evaluacion = get_object_or_404(Evaluacion, id=id)
    return render(request, 'evaluaciones/audiometria_pdf.html', {'evaluacion': evaluacion})

def editar_audiometria(request, id):
    evaluacion = get_object_or_404(Evaluacion, id=id)
    audiometria = getattr(evaluacion, 'audiometria', None)
    
    if not audiometria:
        audiometria = Audiometria.objects.create(evaluacion=evaluacion)

    if request.method == "POST":
        # 1. EVALUACIÓN (Observaciones y Archivo)
        evaluacion.observaciones = request.POST.get("observaciones", "")
        if request.FILES.get("archivo"):
            evaluacion.archivo = request.FILES.get("archivo")
        evaluacion.save()

        # 2. AUDIOGRAMA (JSON)
        audiograma_json = request.POST.get("audiograma_json")
        try:
            if audiograma_json:
                audiometria.audiograma = json.loads(audiograma_json)
        except Exception as e:
            print("Error procesando JSON de audiograma:", e)

        # 3. MODO Y PTP
        audiometria.modo = request.POST.get("tipo", "tonal")
        audiometria.ptp_va_od = request.POST.get("ptp_va_od") or None
        audiometria.ptp_vo_od = request.POST.get("ptp_vo_od") or None
        audiometria.ptp_va_oi = request.POST.get("ptp_va_oi") or None
        audiometria.ptp_vo_oi = request.POST.get("ptp_vo_oi") or None

        # 4. LOGOAUDIOMETRÍA
        audiometria.sds_od = request.POST.get("sds_od") or None
        audiometria.sds_oi = request.POST.get("sds_oi") or None
        audiometria.int_od = request.POST.get("int_od") or None
        audiometria.int_oi = request.POST.get("int_oi") or None
        audiometria.mkg_od = request.POST.get("mkg_od") or None
        audiometria.mkg_oi = request.POST.get("mkg_oi") or None

        # 5. ACUMETRÍA
        audiometria.weber_250 = request.POST.get("weber_250", "")
        audiometria.weber_500 = request.POST.get("weber_500", "")
        audiometria.weber_1000 = request.POST.get("weber_1000", "")
        audiometria.rinne_512_od = request.POST.get("rinne_512_od", "")
        audiometria.rinne_512_oi = request.POST.get("rinne_512_oi", "")

        # 6. DETERIORO TONAL
        audiometria.deterioro_test = request.POST.get("deterioro_test", "")
        audiometria.det_500_od = request.POST.get("det_500_od") or None
        audiometria.det_1000_od = request.POST.get("det_1000_od") or None
        audiometria.det_2000_od = request.POST.get("det_2000_od") or None
        audiometria.det_4000_od = request.POST.get("det_4000_od") or None
        audiometria.det_500_oi = request.POST.get("det_500_oi") or None
        audiometria.det_1000_oi = request.POST.get("det_1000_oi") or None
        audiometria.det_2000_oi = request.POST.get("det_2000_oi") or None
        audiometria.det_4000_oi = request.POST.get("det_4000_oi") or None

        # 7. TINNITUS
        audiometria.tin_presente = request.POST.get("tin_presente") == "on"
        audiometria.tin_ausente = request.POST.get("tin_ausente") == "on"
        audiometria.tin_ocasional = request.POST.get("tin_ocasional") == "on"
        audiometria.tin_examen_positivo = request.POST.get("tin_examen_positivo") == "on"
        audiometria.tin_od = request.POST.get("tin_od") == "on"
        audiometria.tin_oi = request.POST.get("tin_oi") == "on"
        audiometria.tin_bilateral = request.POST.get("tin_bilateral") == "on"
        audiometria.tin_tono_puro = request.POST.get("tin_tono_puro") == "on"
        audiometria.tin_ruido_blanco = request.POST.get("tin_ruido_blanco") == "on"
        audiometria.tin_ruido_banda = request.POST.get("tin_ruido_banda") == "on"
        audiometria.tin_continuo = request.POST.get("tin_continuo") == "on"
        audiometria.tin_pulsatil = request.POST.get("tin_pulsatil") == "on"
        audiometria.tin_fluctuante = request.POST.get("tin_fluctuante") == "on"

        audiometria.save()
        return redirect('ver_paciente', id=evaluacion.paciente.id)

    return render(request, 'evaluaciones/editar_audiometria.html', {
        'evaluacion': evaluacion
    })

def eliminar_evaluacion(request, id):
    evaluacion = get_object_or_404(Evaluacion, id=id)
    paciente_id = evaluacion.paciente.id

    evaluacion.delete()

    return redirect('ver_paciente', id=paciente_id)


def crear_impedanciometria(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        Evaluacion.objects.create(
            paciente=paciente,
            tipo='impedanciometria',
            observaciones=request.POST.get("observaciones"),
            archivo=request.FILES.get("archivo")
        )
        return redirect('ver_paciente', paciente_id)

    return render(request, 'evaluaciones/impedanciometria_form.html', {
        'paciente': paciente,
        'edad': paciente.edad
    })


def crear_otoscopia(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        evaluacion = Evaluacion.objects.create(
            paciente=paciente,
            tipo='otoscopia',
            observaciones=request.POST.get("observaciones", ""),
            archivo=request.FILES.get("archivo")
        )

        Otoscopia.objects.create(
            evaluacion=evaluacion,
            cae_od=request.POST.get("cae_od", ""),
            membrana_od=request.POST.get("membrana_od", ""),
            cae_oi=request.POST.get("cae_oi", ""),
            membrana_oi=request.POST.get("membrana_oi", "")
        )

        return redirect('ver_paciente', paciente_id)

    return render(request, 'evaluaciones/otoscopia_form.html', {
        'paciente': paciente,
        'edad': paciente.edad
    })

def ver_otoscopia(request, id):
    evaluacion = get_object_or_404(Evaluacion, id=id)
    otoscopia = getattr(evaluacion, 'otoscopia', None)
    
    return render(request, 'evaluaciones/ver_otoscopia.html', {
        'evaluacion': evaluacion,
        'otoscopia': otoscopia
    })

def editar_otoscopia(request, id):
    evaluacion = get_object_or_404(Evaluacion, id=id)
    otoscopia = getattr(evaluacion, 'otoscopia', None)
    
    if not otoscopia:
        otoscopia = Otoscopia.objects.create(evaluacion=evaluacion)

    if request.method == "POST":
        evaluacion.observaciones = request.POST.get("observaciones", "")
        if request.FILES.get("archivo"):
            evaluacion.archivo = request.FILES.get("archivo")
        evaluacion.save()

        otoscopia.cae_od = request.POST.get("cae_od", "")
        otoscopia.membrana_od = request.POST.get("membrana_od", "")
        otoscopia.cae_oi = request.POST.get("cae_oi", "")
        otoscopia.membrana_oi = request.POST.get("membrana_oi", "")
        otoscopia.save()

        return redirect('ver_paciente', id=evaluacion.paciente.id)

    return render(request, 'evaluaciones/editar_otoscopia.html', {
        'evaluacion': evaluacion,
        'otoscopia': otoscopia,
        'paciente': evaluacion.paciente
    })


def crear_evaluacion_otro(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        Evaluacion.objects.create(
            paciente=paciente,
            tipo='otro',
            observaciones=request.POST.get("observaciones"),
            archivo=request.FILES.get("archivo")
        )
        return redirect('ver_paciente', paciente_id)

    return render(request, 'evaluaciones/otro_form.html', {
        'paciente': paciente,
        'edad': paciente.edad
    })