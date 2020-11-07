from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category, SubCategory, DatosPer

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

def crear_articulo(request, title, content, public):

    articulo = Article(
        title = title,
        content = content,
        public = public

    )

    articulo.save()
    
    return HttpResponse(f"Articulo creado <strong> {articulo.title} - {articulo.content} </strong>:")

def persona(request, apellidos, nombres, profesion, certificado,  pais, provincia, direccion, correo, telefono):

    persona = DatosPer(
        apellidos = apellidos,
        nombres = nombres,
        profesion = profesion,
        certificado = certificado,
        pais = pais,
        provincia = provincia,
        direccion = direccion,
        correo = correo,
        telefono = telefono
    )

    persona.save()

    return HttpResponse(f"Persona creada <h3><strong> {persona.apellidos} - {persona.nombres} - {persona.profesion} - {persona.certificado} - {persona.pais} - {persona.provincia} - {persona.direccion} - {persona.telefono} </strong></h3>")     

def lista_persona(request, apellidos, nombres, pais, provincia):

    persona = DatosPer.objects.get(apellidos=apellidos, nombres=nombres, pais=pais, provincia=provincia)
    
    return HttpResponse(f"Persona: <br/> <strong> 'Codigo :' {persona.id} <br/> 'Apellidos :' {persona.apellidos} <br/> 'Nombres :' {persona.nombres} <br/> 'Profesion :' {persona.profesion} <br/> 'Certificados :' {persona.certificado} <br/> 'Pais : ' {persona.pais} <br/> 'Provincia :' {persona.provincia} <br/> 'Direccion : ' {persona.direccion} <br/> 'Telefono :' {persona.telefono} <br/></strong>")
   
   

def articulo(request, title, content):

    articulo = Article.objects.get(title=title, content=content)
    
    return HttpResponse(f"Articulo: <br/> <strong> {articulo.id} {articulo.title} {articulo.content} </strong>")

