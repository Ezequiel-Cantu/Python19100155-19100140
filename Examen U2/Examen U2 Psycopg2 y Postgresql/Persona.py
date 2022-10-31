from logger_base import log
class Persona:
    def __init__(self,id_persona=None,nombre=None,edad=None,correo=None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._edad = edad
        self._correo = correo

    def __str__(self) -> str:
        cadena = self.id_persona + ", " + self.nombre + ", " + self.edad + ", " + self.correo
        return cadena

@property
def idPersona(self):
    return self._id_persona
    
@idPersona.setter
def idPersona(self,id_persona):
    self._id_persona=id_persona

@property
def Nombre(self):
    return self._nombre
@Nombre.setter
def Nombre(self,nombre):
    self._nombre = nombre

@property
def Correo(self):
    return self._correo
@Correo.setter
def Correo(self,correo):
    self._correo = correo

@property
def Edad(self):
    return self._edad
@Edad.setter
def Edad(self,edad):
    self._edad = edad