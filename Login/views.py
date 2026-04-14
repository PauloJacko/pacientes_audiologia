from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Paciente
from django.db.models import Q


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
def crear_paciente(request):
    if request.method == 'POST':
        Paciente.objects.create(
            nombre=request.POST['nombre'],
            rut=request.POST['rut'],
            telefono=request.POST.get('telefono'),
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            direccion=request.POST.get('direccion'),
        )
    return redirect('dashboard')


@login_required
def ver_paciente(request, id):
    paciente = Paciente.objects.get(id=id)

    return render(request, 'Login/ver_paciente.html', {
        'paciente': paciente
    })


