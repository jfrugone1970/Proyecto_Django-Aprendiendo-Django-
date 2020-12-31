from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def articulo(request):

    # sacar articulos
    articles = Article.objects.all()

    # paginas de articulos
    paginator = Paginator(articles, 2)

    # recoger el numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
            
    return render(request, 'articles/list.html',{
        'title':'Listado de Articulos',
        'articles':page_articles
        
    })

@login_required(login_url="login")
def categoria(request, category_id):

    categories = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request, 'categories/categories.html', {
        'title':'Listado de Categorias',
        'categories':categories,
        'articles':articles
    
    })

@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
        'article':article
    })    
