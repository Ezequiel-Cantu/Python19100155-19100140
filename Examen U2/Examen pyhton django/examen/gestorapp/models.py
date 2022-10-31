from django.db import models


# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    def __str__(self):
        return (f'Nombre: {self.nombre},  Pais: {self.pais}')

class Obra(models.Model):
    nombre = models.CharField(max_length=255)
    artista = models.ForeignKey(Artista,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return (f'Nombre: {self.nombre}, Artista: {self.artista}')


class Museo(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return (f'Nombre: {self.nombre}')

class Disciplina(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return (f'Nombre: {self.nombre}')
class Escuela(models.Model):
    nombre = models.CharField(max_length=255)
    disciplina = models.ForeignKey(Disciplina,on_delete = models.SET_NULL,null=True)
    def __str__(self):
        return (f'Nombre: {self.nombre}, Disciplina: {self.disciplina}')


