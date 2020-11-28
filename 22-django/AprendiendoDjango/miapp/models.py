from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="articles")
    public = models.BooleanField(default=True,verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="editado")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id']

    def __str__(self):
        
        if self.public:
            publico = "(publicado)"
        else:
            publico = "(privado)"

        return f"{self.title} {self.content}  {publico}"


class Category(models.Model):
    name = models.CharField(max_length=150,default='Informatica',null=False, verbose_name="Nombre")
    description = models.CharField(max_length=250,default='Desarrollo Web',null=False, verbose_name="descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="editado")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']
    

class SubCategory(models.Model):
    name = models.CharField(max_length=250,default='Informatica',null=False, verbose_name="nombre")
    description = models.CharField(max_length=200,default='Desarrollo Web con Django',null=False, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="editado")

    class Meta:
        verbose_name = "SubCategoria"
        verbose_name_plural = "SubCategorias"
        ordering = ['id']

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

class DatosPer(models.Model):
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    profesion = models.CharField(max_length=250, default='null')
    certificado = models.TextField(default='null')
    image = models.ImageField(default='null', upload_to="person")
    pais = models.CharField(max_length=200)
    provincia = models.CharField(max_length=60)
    direccion = models.TextField()
    correo = models.TextField()
    telefono = models.TextField()
    fecha_ing = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)


    
        




    

