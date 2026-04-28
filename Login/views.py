from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Paciente, Anamnesis
from django.db.models import Q
from evaluaciones.models import Evaluacion


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'Login/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'Login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def eliminar_paciente(request, id):
    if request.method == 'POST':
        paciente = Paciente.objects.get(id=id)
        paciente.delete()
    return redirect('dashboard')

@login_required
def dashboard_view(request):

    nombre = request.GET.get('nombre')
    rut = request.GET.get('rut')

    pacientes = Paciente.objects.all().order_by('-creado')

    if nombre:
        pacientes = pacientes.filter(nombre__icontains=nombre)

    if rut:
        pacientes = pacientes.filter(rut__icontains=rut)

    return render(request, 'Login/dashboard.html', {
        'pacientes': pacientes
    })

@login_required
def ver_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    anamnesis = paciente.anamnesis.all().order_by('-fecha')
    evaluaciones = paciente.evaluaciones.all().order_by('-fecha')
    
    audiometrias = evaluaciones.filter(tipo='audiometria')
    impedancias = evaluaciones.filter(tipo='impedanciometria')
    otoscopias = evaluaciones.filter(tipo='otoscopia')
    otros = evaluaciones.filter(tipo='otro')

    return render(request, 'Login/ver_paciente.html', {
        'paciente': paciente,
        'anamnesis': anamnesis,
        'audiometrias': audiometrias,
        'impedancias': impedancias,
        'otoscopias': otoscopias,
        'otros': otros,
    })

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        paciente = Paciente.objects.create(
            nombre=request.POST['nombre'],
            rut=request.POST['rut'],
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            direccion=request.POST.get('direccion'),
            prevision=request.POST.get('prevision'),
        )

        return redirect('ver_paciente', paciente.id)

    return redirect('dashboard')

@require_POST
@login_required
def crear_anamnesis(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    Anamnesis.objects.create(
        paciente=paciente,
        motivo_consulta=request.POST.get('motivo_consulta'),
        antecedentes_medicos=request.POST.get('antecedentes_medicos'),
        antecedentes_auditivos=request.POST.get('antecedentes_auditivos'),

        hipoacusia=bool(request.POST.get('hipoacusia')),
        tinnitus=bool(request.POST.get('tinnitus')),
        vertigo=bool(request.POST.get('vertigo')),
        otalgia=bool(request.POST.get('otalgia')),

        exposicion_ruido=bool(request.POST.get('exposicion_ruido')),
        uso_audifonos=bool(request.POST.get('uso_audifonos')),

        medicamentos=request.POST.get('medicamentos'),
        alergias=request.POST.get('alergias'),
        observaciones=request.POST.get('observaciones'),
    )

    return redirect('ver_paciente', paciente.id)

@login_required
def editar_anamnesis(request, anamnesis_id):
    anamnesis = get_object_or_404(Anamnesis, id=anamnesis_id)

    if request.method == "POST":
        anamnesis.motivo_consulta = request.POST.get("motivo_consulta")
        anamnesis.antecedentes_medicos = request.POST.get("antecedentes_medicos")
        anamnesis.antecedentes_auditivos = request.POST.get("antecedentes_auditivos")
        anamnesis.observaciones = request.POST.get("observaciones")
        anamnesis.medicamentos = request.POST.get("medicamentos")
        anamnesis.alergias = request.POST.get("alergias")

        anamnesis.hipoacusia = "hipoacusia" in request.POST
        anamnesis.tinnitus = "tinnitus" in request.POST
        anamnesis.vertigo = "vertigo" in request.POST
        anamnesis.otalgia = "otalgia" in request.POST

        anamnesis.exposicion_ruido = "exposicion_ruido" in request.POST
        anamnesis.uso_audifonos = "uso_audifonos" in request.POST

        anamnesis.save()

        return redirect("ver_paciente", id=anamnesis.paciente.id)

@login_required
def eliminar_anamnesis(request, id):
    anamnesis = get_object_or_404(Anamnesis, id=id)
    paciente_id = anamnesis.paciente.id

    anamnesis.delete()

    return redirect('ver_paciente', id=paciente_id)