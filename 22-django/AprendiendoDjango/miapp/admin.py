from django.contrib import admin
from .models import Article, Category, SubCategory, DatosPer

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
      readonly_fields = ('created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
      readonly_fields = ('created_at', 'updated_at')

class SubCategoryAdmin(admin.ModelAdmin):
      readonly_fields = ('created_at', 'updated_at') 

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(DatosPer)




