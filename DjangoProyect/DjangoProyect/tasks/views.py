from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import Producto, Usuario
from .forms import UsuarioForm

# Funcion de index
def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'usuarios_views/registerUser.html')

def list_usuarios(request):
    return render(request, 'usuarios_views/panelusuarios.html')

