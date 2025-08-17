from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from presentation.forms import UsuarioForm
from core.use_cases.usuario_case_uses import CrearUsuario
from infrastructure.repositories.usuario_repository_django import UsuarioRepositoryDjango
from django.contrib.auth.models import User

def registerPage(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario_data = {
                "username": form.cleaned_data["username"],
                "email": form.cleaned_data["email"],
                "password": form.cleaned_data["password"],
                "plan": "free",
            }

            try:
                caso = CrearUsuario(UsuarioRepositoryDjango())
                usuario = caso.execute(usuario_data)
                login(request, usuario)  
                return redirect('home')

            except Exception as e:
                messages.error(request, f'Ocurrió un error al registrar: {str(e)}')
        else:
            messages.error(request, 'Datos inválidos en el formulario')

    return render(request, 'login/login_register.html', {'form': form})



def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")

    context = {'page': page}
    return render(request, 'login/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')