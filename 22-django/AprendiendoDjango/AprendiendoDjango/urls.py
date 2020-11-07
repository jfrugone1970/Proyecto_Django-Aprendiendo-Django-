"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importar mi app con mi vista
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('inicio/<str:nombre>',views.index, name="inicio"),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('paginas-pruebas/', views.pagina, name="pagina"),
    path('paginas-pruebas/<int:redirigir>', views.pagina, name="pagina"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto/<str:profesion>/<str:nombre>', views.contacto, name="contacto"),
    path('contacto/<str:profesion>/<str:nombre>/<str:apellido>', views.contacto, name="contacto"),
    path('estudiante/', views.estudiante, name="estudiante"),
    path('estudiante/<str:nombre>', views.estudiante, name="estudiante"),
    path('estudiante/<str:nombre>/<str:apellido>/', views.estudiante, name="estudiante"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>/', views.crear_articulo, name="crea_articulo"),
    path('mostrar-articulo/<str:title>/<str:content>/', views.articulo, name="mostrar"),
    path('crea-persona/<str:apellidos>/<str:nombres>/<str:pais>/<str:provincia>/<str:direccion>/<str:correo>/<str:telefono>/',views.persona, name="persona"),
    path('lista/<str:apellidos>/<str:nombres>/<str:pais>/<str:provincia>/', views.lista_persona, name="mostrar_p")
    
]
