from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=150,default='Informatica',null=False)
    description = models.CharField(max_length=250,default='Desarrollo Web',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class SubCategory(models.Model):
    name = models.CharField(max_length=250,default='Informatica',null=False)
    description = models.CharField(max_length=200,default='Desarrollo Web con Django',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    image = models.ImageField(default='null')
    pais = models.CharField(max_length=200)
    provincia = models.CharField(max_length=60)
    direccion = models.TextField()
    correo = models.TextField()
    telefono = models.TextField()
    fecha_ing = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)


    
        




    
