from django.shortcuts import redirect, render
from .models import Curso, Comision, Alumno
from .forms import CursoForm , ComisionForm, AlumnoForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request,"core/about.html" )

@login_required
def curso_list(request):
    query = Curso.objects.all()
    context = {"object_list": query}
    return render(request, "curso/curso_list.html", context)

@login_required
def curso_create(request):
    if request.method == "GET":
        form = CursoForm()
    if request.method == "POST":
         form = CursoForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect("curso:curso_list")
    return render(request, "curso/curso_form.html" , {"form" :form})


@login_required
def comision_list(request):
    query = Comision.objects.all()
    context = {"object_list": query}
    return render(request, "curso/comision_list.html", context)

@login_required
def comision_create(request):
    if request.method == "GET":
        form = ComisionForm()
    if request.method == "POST":
            form = ComisionForm(request.POST)
            if form.is_valid():
              form.save()
            return redirect("curso/comision_list")
    return render(request, "curso/comision_form.html" , {"form" :form})




@login_required
def alumno_list(request):
    query = Alumno.objects.all()
    context = {"object_list": query}
    return render(request, "curso/alumno_list.html", context)

@login_required
def alumno_create(request):
    if request.method == "GET":
        form = AlumnoForm()
    if request.method == "POST":
            form = AlumnoForm(request.POST)
            if form.is_valid():
               form.save()
            return redirect("curso:alumno_list")
    return render(request, "curso/alumno_form.html" , {"form" :form})



def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Guardar el usuario
            form.save()
            messages.success(request, "Usuario registrado correctamente. Ahora puedes iniciar sesión.")
            return redirect('curso:login')  # Redirige a la página de login
    else:
        form = UserRegistrationForm()
    return render(request, 'curso/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:index')  # Redirige a la página principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'curso/login.html')



def logout_user(request):
    logout(request)
    return redirect('curso:login')