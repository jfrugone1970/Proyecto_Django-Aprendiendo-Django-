from django.shortcuts import render
from .models import Page
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
       "page":page
    })

def crea_pagina(request):

   if request.method == "POST":
      title = request.POST['title']
      content = request.POST['content']
      slug = request.POST['slug']
      order = request.POST['order']
      visible = request.POST['visible']

   pages = Page(
      title = title,
      content = content,
      slug = slug,
      order = order,
      visible = visible

   )   

   pages.save()
  
   # Crear mensaje flash (que es una sesion que solo se muestra 1 vez)
   messages.success(request, f'Has creado correctamente la pagina {pages.id}')
    
   #return redirect('lista_gen_cat')
   
   return render(request, 'mainapp/index.html',{
      'title':"Inicio",
      'usuario':"ADMIN",
      'clave':"ZZZ"
   })