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

def editar_articulo(request, id, title, content, public):

    articulo = Article.objects.get(pk=id)

    articulo.title = title
    articulo.content = content
    articulo.public = public

    articulo.save()

    return HttpResponse(f"Articulo editado <strong> {articulo.title} - {articulo.content} </strong>:")




def crear_category(request, name, description):

    categoria = Category(
        name = name,
        description = description
    )

    categoria.save()

    return HttpResponse(f"Categoria creada <strong> {categoria.name} - {categoria.description} </strong>")

def editar_categori(request, id, name, description):

    categori = Category.objects.get(pk=id)

    categori.name = name
    categori.description = description

    categori.save()

    return HttpResponse(f"Categoria Editada <strong> {categori.name} - {categori.description} </strong>")    

def lista_categori(request, name, description):

    try:
        
        categoria = Category.objects.get(name=name, description=description)

        response = f"Categoria : <br/> <strong> 'Categoria_id : ' {categoria.id} <br/> 'Categoria_name :' {categoria.name} <br/> 'Descripcion : ' {categoria.description} <br/> </strong>"
    except:
        response = "<h1> No hay Categoria </h2>"

    return HttpResponse(response)


def crear_sub_category(request, name, description):

    subcategori = SubCategory(
        name = name,
        description = description
    )

    subcategori.save()

    return HttpResponse(f"Subcategoria guardada <strong> {subcategori.name} - {subcategori.description} </strong>")

def editar_subcategoria(request, id, name, description):

    subcategori = SubCategory.objects.get(pk=id)

    subcategori.name = name
    subcategori.description = description

    subcategori.save()

    return HttpResponse(f"Subcategoria editada <strong> {subcategori.name} - {subcategori.description} </strong>")


def lista_subcategory(request, name, description):

    try:

        subcategori = SubCategory.objects.get(name=name, description=description)

        response = f"Subcategori: <br/> <strong> 'Subcategori_id : ' {subcategori.id} <br/> 'Subcategori_name :' {subcategori.name} <br/> 'Descripcion : ' {Subcategori.description} <br/> </strong>"
    except:
        response = "<h1>No hay subcategoria </h1>"    

    return HttpResponse(response)


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

def editar_persona(request, id, apellidos, nombres, profesion, certificado, pais, provincia, direccion, correo, telefono):

    persona = DatosPer.objects.get(pk=1)

    persona.apellidos = apellidos
    persona.nombres = nombres
    persona.profesion = profesion
    persona.certificado = certificado
    persona.pais = pais
    persona.provincia = provincia
    persona.direccion = direccion
    persona.correo = correo
    persona.telefono = telefono

    persona.save()

    return HttpResponse(f"Persona Editada <h3><strong> {persona.apellidos} - {persona.nombres} - {persona.profesion} - {persona.certificado} - {persona.pais} - {persona.provincia} - {persona.direccion} - {persona.telefono} </strong></h3>")


def lista_persona(request, apellidos, nombres, pais, provincia):

    try:

        persona = DatosPer.objects.get(apellidos=apellidos, nombres=nombres, pais=pais, provincia=provincia)

        response = f"Persona: <br/> <strong> 'Codigo :' {persona.id} <br/> 'Apellidos :' {persona.apellidos} <br/> 'Nombres :' {persona.nombres} <br/> 'Profesion :' {persona.profesion} <br/> 'Certificados :' {persona.certificado} <br/> 'Pais : ' {persona.pais} <br/> 'Provincia :' {persona.provincia} <br/> 'Direccion : ' {persona.direccion} <br/> 'Telefono :' {persona.telefono} <br/></strong>"
    except:
        response = "<h1> Persona no existe</h1>"    
    
    return HttpResponse(response)
   
   

def articulo(request, title, content):

    try:

        articulo = Article.objects.get(title=title, content=content)

        response = f"Articulo: <br/> <strong> {articulo.id} {articulo.title} {articulo.content} </strong>"
    except:
        response = "<h1> Articulo no encontrado </h1>"

    return HttpResponse(response)

def articulo_gen(request):

    articulos = Article.objects.order_by("title")

    return render(request, 'articulos.html',{
        'articulos':articulos
    })

def borrar_articulos(request, id):

    mensaje = ""
    mensaje1 = ""

    articulos = Article.objects.get(pk=id)

    articulos.delete()

    mensaje = "Se borro articulo exitosamente"
    mensaje1 = "El articulo escogido ya no existe en la tabla"

    return render(request, 'articulos.html',{
        'mensaje':mensaje,
        'mensaje1':mensaje1
    })    

def categoria_gen(request):

    categorias = Category.objects.all()

    return render(request, 'categoria.html',{
        'categorias':categorias
    })

def borrar_categ(request, id):
    mensaje = ""
    mensaje1 = ""

    categorias = Category.objects.get(pk=id)
   
    categorias.delete()
   
    mensaje = "Se borro la categoria exitosamente"
    mensaje1 = "La categoria escogida ya no existe en la tabla"

    return render(request, 'categoria.html',{
        'mensaje':mensaje,
        'mensaje1':mensaje1
        
    })


def subcategori_gen(request):

    subcategorias = SubCategory.objects.all()

    return render(request, 'subcategoria.html',{
        'subcategorias':subcategorias
    })

def borrar_subcategori(request, id):

    mensaje = ""
    mensaje1 = ""

    subcategori = SubCategory.objects.get(pk=id)
    subcategori.delete()

    
    mensaje = "Se borro la subcategoria exitosamente"
    mensaje1 = "La subcategoria escogida ya no existe en la tabla"

    return render(request, 'subcategoria.html',{
        'mensaje':mensaje,
        'mensaje1':mensaje1
        
    })


def personas_gen(request):

    personas = DatosPer.objects.order_by("apellidos")

    return render(request, 'persona.html',{
        'personas':personas
    })            




