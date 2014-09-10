from django.contrib import admin
from news.models import News, Article
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Article, ArticleAdmin)

