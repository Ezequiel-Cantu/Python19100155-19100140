from logger_base import log

class Bailarin:
    def __init__(self,id_bailarin=None,nombre=None, apellido=None,danza=None,nivel=None) -> None:
        self._id_bailarin = id_bailarin
        self._nombre = nombre
        self._apellido = apellido
        self._danza = danza
        self._nivel = nivel

    def __str__(self) -> str:
        cadena = str(self._id_bailarin) + ", " + self._nombre + ", " + self._apellido + ", " + self._danza + ", " + self._nivel
        return cadena

@property
def idBailarin(self):
    return self._id_bailarin
    
@idBailarin.setter
def idBailarin(self,id_bailarin):
    self._id_bailarin=id_bailarin

@property
def Nombre(self):
    return self._nombre
@Nombre.setter
def Nombre(self,_nombre):
    self._nombre = _nombre

@property
def Apellido(self):
    return self._apellido
@Apellido.setter
def Apellido(self,_apellido):
    self._apellido = _apellido

@property
def Danza(self):
    return self._danza
@Danza.setter
def Danza(self,_danza):
    self._danza = _danza

@property
def Nivel(self):
    return self._nivel
@Nivel.setter
def Nivel(self,_nivel):
    self._nivel = _nivel