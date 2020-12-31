from django.urls import path

from . import views

urlpatterns = [
    path('pagina/<str:slug>', views.page, name="page"),
    path('create-full-pagina/', views.crea_pagina, name="create_full_pagina")

]