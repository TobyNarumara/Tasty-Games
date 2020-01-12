from django.contrib import admin

from .models import Genre, Article, Language

admin.site.register(Language)
admin.site.register(Genre)

@admin.register(Article)
class Article(admin.ModelAdmin):
	list_display = ['name', 'img', 'last_update']