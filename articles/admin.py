from django.contrib import admin
from .models import Article

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author_first_name', 'author_last_name', 'category', 'content', 'image', 'created_at')
#     prepopulated_fields = { 'slug': ('title'), }
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'content', 'authors',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)