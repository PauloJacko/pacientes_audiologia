from django.shortcuts import render, redirect, get_object_or_404
from Login.models import Paciente
from .models import Evaluacion

def crear_audiometria(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        Evaluacion.objects.create(
            paciente=paciente,
            tipo='audiometria',
            observaciones=request.POST.get("observaciones"),
            archivo=request.FILES.get("archivo")
        )
        return redirect('ver_paciente', paciente_id)

    return render(request, 'evaluaciones/audiometria_form.html', {
        'paciente': paciente
    })


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
        'paciente': paciente
    })


def crear_otoscopia(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        Evaluacion.objects.create(
            paciente=paciente,
            tipo='otoscopia',
            observaciones=request.POST.get("observaciones"),
            archivo=request.FILES.get("archivo")
        )
        return redirect('ver_paciente', paciente_id)

    return render(request, 'evaluaciones/otoscopia_form.html', {
        'paciente': paciente
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
        'paciente': paciente
    })