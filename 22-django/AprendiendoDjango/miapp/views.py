from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category, SubCategory

# Create your views here.
# MVC - Modelo Vista Controlador -> Acciones(metodos)
# MVT - Modelo Template Vista -> Acciones(metodos)

layout = """

        <h1>Sitio web con Django | Lcdo Jose Fernando Frugone</h1>
        <hr/>
        <ul>
            <li>
                <a href="/inicio">Inicio</a>
            </li>
            <li>
                <a href="/hola-mundo">Hola-mundo</a>
            </li>
            <li>
                <a href="/paginas-pruebas">Paginas</a>
            </li>
            <li>
                <a href="/contacto/Lcdo./Jose Fernando/Frugone Jaramillo">Contacto</a>
            </li>
            <li>
                 <a href="/estudiante/Luis Andres/Garcia Moran">Estudiante</a>
            </li>

        </ul>
        <hr/>

"""

def index(request, nombre=""):

    year = 1970

    bisiesto = []

    while year <= 2020:

        if year % 4 == 0:

            bisiesto.append(f"{str(year)}")
      
        year += 1

    dato1 = 1950
    periodo = range(dato1, 2021)
    nombre = "Lcdo. Jose Fernando Frugone Jaramillo"

    return render(request, 'index.html', {
        'titulo':'Inicio',
        'nombre':nombre,
        'bisiesto':bisiesto,
        'periodo':periodo
        
    }) 

def hola_mundo(request):

    return render(request, 'hola_mundo.html') 

def pagina(request, redirigir = 0):

    
    if redirigir == 1:
        return redirect('/index')
    
    elif redirigir == 2:
        return redirect('/hola-mundo')
    
    elif redirigir == 3:
        return redirect('contacto',profesion="Lcdo",nombre="Jose Fernando",apellido="Frugone Jaramillo")
    
    elif redirect == 4:
        return redirect('estudiante',nombre="Juan Pablo",apellido="Castro Gonzalez")        

    return render(request, 'pagina.html')

def contacto(request, profesion="", nombre="", apellido=""):

    return render(request, 'contacto.html', {
        'titulo':'Pagina de contacto',
        'profesion':profesion,
        'nombre':nombre,
        'apellido':apellido
       
    })

def estudiante(request, nombre="", apellido=""):

    lista = [{
        'nombre':'Antonio',
        'apellido':'Garcia'
    },
    {
        'nombre':'Pablo',
        'apellido':'Rosales'
    },
    {
        'nombre':'Alejandro',
        'apellido':'Andrade'
    },
    {
        'nombre':'Luis',
        'apellido':'Castro'
    },
    {
        'nombre':'Eduardo',
        'apellido':'Medina'
    },
    {
        'nombre':'Carlos',
        'apellido':'Gonzalez'
    }
    ]


    return render(request, 'estudiante.html', {
        'titulo':'Pagina de estudiante',
        'lista':lista
    })

def crear_articulo(request):

    articulo = Article(
        title = 'Primer Articulo',
        content = 'Contenido del articulo',
        public = True,

    )

    articulo.save()
    
    return HttpResponse("Usuario creado :")                        




