from django.shortcuts import render
from gestorapp.models import Obra,Artista,Museo,Escuela,Disciplina
# Create your views here.
def bienvenido(request):
    disciplinas = Disciplina.objects.order_by('id')
    artistas = Artista.objects.order_by('id')
    obras = Obra.objects.order_by('id')
    escuelas = Escuela.objects.order_by('id')
    museos = Museo.objects.order_by('id')
    return render(request,'bienvenido.html',{'disciplinas':disciplinas,'artistas':artistas,'obras':obras,'escuelas':escuelas,'museos':museos})