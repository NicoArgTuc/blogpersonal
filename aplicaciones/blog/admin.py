from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import * 

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion',)
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'slug', 'categoria', 'autor']
    list_display = ('titulo', 'slug', 'categoria', 'autor', 'fecha_creacion',)
    resource_class = PostResource

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
