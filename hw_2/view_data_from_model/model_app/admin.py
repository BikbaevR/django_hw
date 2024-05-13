from django.contrib import admin

from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'creations_date']
    search_fields = ['name', 'creations_date']
    list_filter = ['creations_date']


admin.site.register(Article, ArticleAdmin)