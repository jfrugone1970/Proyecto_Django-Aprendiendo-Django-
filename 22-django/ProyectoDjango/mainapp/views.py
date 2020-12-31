from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
 

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html',{
       'title':'Inicio',
       'title2':'Formulario para creacion de paginas'
    })

def about(request):

    return render(request, 'mainapp/about.html',{
        'title':'Sobre nosotros'
    })

def special(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            if user.is_superuser == False:

               messages.warning(request, 'No eres usuario Administrador no puedes crear una pagina') 

            return render(request, 'mainapp/special.html',{
                'usuario':username,
                'clave':password,
                'title':'Pantalla de Menu de creacion de Paginas'
            })

        else:
            messages.warning(request, 'No te has identificado correctamente!!')        

    return render(request, 'mainapp/index.html',{
        'title':'Inicio'
    })       

def create_pagina(request):

    
    return render(request, 'pages/crear.html',{
        'title':'Creacion de Paginas'
       
    })

def register_page(request):

    if request.user.is_authenticated:

       return redirect('inicio')

    else:

        register_form = RegisterForm()

        if request.method == "POST":
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente!!')

                return redirect('inicio')


    return render(request, 'users/register.html',{
        'title':'Registro',
        'register_form':register_form
    })

def login_page(request):

    if request.user.is_authenticated:

        return redirect('inicio')

    else:
   
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                """
                 Validar si es superusuario
                """
                if user.is_superuser == True:

                    messages.success(request, 'Usuario es un Superusuario o Administrador!!')

                login(request, user)
                return redirect('inicio')

            else:
                messages.warning(request, 'No te has identificado correctamente!!')        

    return render(request, 'users/login.html',{
        'title':'Identificate',
        'title_especial':'Operacion especial para el administrador de la pagina'
    })

def logout_user(request):

    logout(request)
    return redirect('login')
