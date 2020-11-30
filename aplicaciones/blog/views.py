from django.shortcuts import render
from django.db.models import Q
from .models import *

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True
        ).distinct()
    return render(request, 'index.html', {'posts': posts})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
       categoria = Categoria.objects.get(nombre = 'General'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre = 'General')
        ).distinct()
    return render(request, 'generales.html', {'posts': posts})

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
        categoria = Categoria.objects.get(nombre = 'Programacion'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre = 'Programacion')
        ).distinct()
    return render(request, 'programacion.html', {'posts': posts})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
        categoria = Categoria.objects.get(nombre = 'Tutoriales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre = 'Tutoriales')
        ).distinct()
    return render(request, 'tutoriales.html', {'posts': posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
        categoria = Categoria.objects.get(nombre = 'Tecnologia'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre = 'Tecnologia')
        ).distinct()
    return render(request, 'tecnologia.html', {'posts': posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
        categoria = Categoria.objects.get(nombre = 'Video juegos'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre = 'Video juegos')
        ).distinct()
    return render(request, 'videojuegos.html', {'posts': posts})

def detallePost(request, slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'post.html', {'detalle_post': post})