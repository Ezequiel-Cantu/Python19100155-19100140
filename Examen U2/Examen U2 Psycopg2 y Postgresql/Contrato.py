from logger_base import log

class Contrato:
    def __init__(self,idContrato=None,noContrato=None,costo=None,fechaInicio=None, fechaFin= None) -> None:
        self._id_Contrato = idContrato
        self._noContrato = noContrato
        self._costo = costo
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin

    def __str__(self) -> str:
        cadena = self.idContrato + ", " + self.noContrato + ", " + self.costo + ", " + self.fechaInicio + "," + self.fechaFin
        return cadena

@property
def idContrato(self):
    return self._id_Contrato
    
@idContrato.setter
def idContrato(self,idContrato):
    self._id_Contrato=idContrato
    
@property
def NoContrato(self):
    return self._noContrato
@NoContrato.setter
def NoContrato(self,noContrato):
    self._noContrato = noContrato

@property
def Costo(self):
    return self._costo
@Costo.setter
def Costo(self,costo):
    self._costo = costo

@property
def FechaFin(self):
    return self._fechaFin
@FechaFin.setter
def FechaFin(self,fechaFin):
    self._fechaFin = fechaFin
    
