from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    pais = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return (f'Nombre: {self.nombre} '
                f'Edad: {self.edad} '
                f'Pais: {self.pais} ')


class Libro(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return (f'Nombre: {self.nombre} '
                f'Genero: {self.genero} '
                f'Autor: {self.autor} ')
    
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    fechafundacion = models.DateField()
    
    def __str__(self) -> str:
        return (f'Nombre: {self.nombre} '
                f'Pais: {self.pais} '
                f'Fecha de Fundacion: {self.fechafundacion.__str__()} ')

class Editora(models.Model):
    nombre=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return (f'Nombre: {self.nombre} ')