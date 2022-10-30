"""practica2 URL Configuration

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
from entidades.views import detalleAutor,nuevaAutor,editarAutor,eliminarAutor,nuevaBiblioteca,eliminarBiblioteca,detalleBiblioteca,editarBiblioteca,eliminarLibro,detalleLibro,editarLibro,nuevaLibro,eliminarEditora,detalleEditora,editarEditora,nuevaEditora
from prac2app.views import bienvenido
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='index'),
    path('autor/agregar/',nuevaAutor),
    path('autor/editar/<int:id>',editarAutor),
    path('autor/eliminar/<int:id>',eliminarAutor),
    path('autor/detalle/<int:id>',detalleAutor),
    path('biblioteca/agregar/',nuevaBiblioteca),
    path('biblioteca/editar/<int:id>',editarBiblioteca),
    path('biblioteca/eliminar/<int:id>',eliminarBiblioteca),
    path('biblioteca/detalle/<int:id>',detalleBiblioteca),
    path('libro/agregar/',nuevaLibro),
    path('libro/editar/<int:id>',editarLibro),
    path('libro/eliminar/<int:id>',eliminarLibro),
    path('libro/detalle/<int:id>',detalleLibro),
    path('editora/agregar/',nuevaEditora),
    path('editora/editar/<int:id>',editarEditora),
    path('editora/eliminar/<int:id>',eliminarEditora),
    path('editora/detalle/<int:id>',detalleEditora)
]
