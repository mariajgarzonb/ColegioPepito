import queue
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Curso, Alumno
from colegio.forms import AlumnoForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def gestion_cursos(request):
    cursos_listados = Curso.objects.all()
    data = {
        'titulo': 'Gestión de Cursos',
        'cursos': cursos_listados
    }
    return render(request, "gestionCursos.html", data)

# @login_required


class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        return Curso.objects.all().order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Cursos'
        return context


@login_required
def registrar_curso(request):
    nombre = request.POST['txtNombre']
    horas = request.POST['numHoras']
    curso = Curso.objects.create(nombre=nombre, horas=horas)
    return redirect('gestion_cursos')


@login_required
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('gestion_cursos')


@login_required
def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': 'Edición de Curso',
        'curso': curso
    }
    return render(request, "edicionCurso.html", data)


@login_required
def editar_curso(request):
    id = int(request.POST['id'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('gestion_cursos')


def contacto(request):
    return render(request, "contacto.html")


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    user = authenticate(
        request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o contraseña incorrecta."})
    login(request, user)
    return redirect('gestion_cursos')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    if request.POST["password1"] == request.POST["password2"]:
        try:
            user = User.objects.create_user(
                request.POST["username"], password=request.POST["password1"])
            user.save()
            login(request, user)
            return redirect('home')
        except IntegrityError:
            return render(request, 'signup.html', {"form": UserCreationForm, "error": "El usuario ya existe."})
    return render(request, 'signup.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})

# ... Código Alumnos ...


@login_required
def gestion_alumnos(request):
    alumnos_listados = Alumno.objects.all()
    context = {
        'titulo': 'Gestión de Alumnos',
        'alumnos': alumnos_listados
    }
    return render(request, 'gestionAlumnos.html', context)

# @login_required


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'gestionAlumnos.html'
    context_object_name = 'alumnos'
    ordering = ['-id']
    paginate_by = 10


@login_required
def registrar_alumno(request):
    dni = request.POST['txtDni']
    nombre = request.POST['txtNombre']
    apellidos = request.POST['txtApellidos']

    alumno = Alumno.objects.create(
        dni=dni, nombre=nombre, apellidos=apellidos)
    return redirect('gestion_alumnos')


@login_required
def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    return redirect('gestion_alumnos')


@login_required
def edicion_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    data = {
        'titulo': 'Edición de Alumno',
        'alumno': alumno
    }
    return render(request, "edicionAlumno.html", data)


@login_required
def editar_alumno(request):
    id = int(request.POST['id'])
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    alumno = Alumno.objects.get(id=id)
    alumno.dni = dni
    alumno.nombre = nombre
    alumno.apellidos = apellidos
    alumno.save()
    return redirect('gestion_alumnos')
