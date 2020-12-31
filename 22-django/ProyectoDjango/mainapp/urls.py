from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('especial/', views.special, name="especial"),
    path('create-page/', views.create_pagina, name="create_pagina"),
    path('registro/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]