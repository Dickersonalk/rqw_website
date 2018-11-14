from django.contrib import admin
from Article.models import Type,Picture,Article
# Register your models here.
admin.site.register(Type)
admin.site.register(Picture)
admin.site.register(Article)