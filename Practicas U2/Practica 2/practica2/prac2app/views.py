from django.shortcuts import render
from django.http import HttpResponse
from entidades.views import Libro,Autor,Biblioteca,Editora
# Create your views here.
def bienvenido(request):
    libros = Libro.objects.order_by('id')
    bibliotecas = Biblioteca.objects.order_by('id')
    editors = Editora.objects.order_by('id')
    autores = Autor.objects.order_by('id')
    return render(request,'bienvenido.html',{'libros':libros,'bibliotecas':bibliotecas,'autores':autores,'editors':editors})