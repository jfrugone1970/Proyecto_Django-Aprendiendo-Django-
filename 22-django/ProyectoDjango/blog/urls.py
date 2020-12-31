from django.urls import path
from . import views


urlpatterns = [
    path('articulos/', views.articulo, name="list_article"),
    path('categoria/<int:category_id>', views.categoria, name="categorias"),
    path('detalles/<int:article_id>', views.article, name="detalle")
]