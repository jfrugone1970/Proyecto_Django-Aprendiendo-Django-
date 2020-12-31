from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'user', 'categories')
    list_display = ('title', 'user', 'public','created_at')
    list_filter = ('public', 'user', 'categories')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
            
        obj.save()



# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
