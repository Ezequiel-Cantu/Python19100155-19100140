from logger_base import log

class Contrato_Persona:
    def __init__(self,idContrato=None,idPersona=None) -> None:
        self._id_Persona = idPersona
        self._id_Contrato = idContrato

    def __str__(self) -> str:
        cadena = self.idContrato + ", " + self.idPersona
        return cadena
    
@property
def idPersona(self):
    return self._id_Persona
    
@idPersona.setter
def idPersona(self,idPersona):
    self._id_Persona=idPersona

@property
def idContrato(self):
    return self._id_Contrato
    
@idContrato.setter
def idContrato(self,idContrato):
    self._id_Contrato=idContrato