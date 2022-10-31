"""examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestorapp.views import detalleArtista,detalleDisciplina,detalleEscuela,detalleMuseo,detalleObra,editarArtista,editarDisciplina,editarEscuela,editarMuseo,editarObra,eliminarArtista,eliminarDisciplina,eliminarEscuela,eliminarMuseo,eliminarObra,nuevaArtista,nuevaDisciplina,nuevaEscuela,nuevaMuseo,nuevaObra
from webapp.views import bienvenido
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='index'),
    #artista
    path('artista/agregar',nuevaArtista),
    path('artista/editar/<int:id>',editarArtista),
    path('artista/eliminar/<int:id>',eliminarArtista),
    path('artista/detalle/<int:id>',detalleArtista),
    ##obra
    path('obra/agregar',nuevaObra),
    path('obra/editar/<int:id>',editarObra),
    path('obra/eliminar/<int:id>',eliminarObra),
    path('obra/detalle/<int:id>',detalleObra),
    #museo
    path('museo/agregar',nuevaMuseo),
    path('museo/editar/<int:id>',editarMuseo),
    path('museo/eliminar/<int:id>',eliminarMuseo),
    path('museo/detalle/<int:id>',detalleMuseo),
    #escuela
    path('escuela/agregar',nuevaEscuela),
    path('escuela/editar/<int:id>',editarEscuela),
    path('escuela/eliminar/<int:id>',eliminarEscuela),
    path('escuela/detalle/<int:id>',detalleEscuela),
    #disciplina
    path('disciplina/agregar',nuevaDisciplina),
    path('disciplina/editar/<int:id>',editarDisciplina),
    path('disciplina/eliminar/<int:id>',eliminarDisciplina),
    path('disciplina/detalle/<int:id>',detalleDisciplina),
]
