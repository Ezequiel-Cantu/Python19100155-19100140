from ContratoPersona import Contrato_Persona
from Conexion import Conexion
from logger_base import log
from psycopg2 import pool

class ContratoPersonaDao:
    _SELECCIONAR = "SELECT * FROM contrato_persona ORDER BY \"idPersona\""
    _INSERTAR = "INSERT INTO contrato_persona(\"idPersona\",\"idContrato\") Values(%s,%s)"
    _ACTUALIZAR = "UPDATE contrato_persona SET idPersona=%s,idContrato=%s WHERE idPersona = %s"
    _ELIMINAR = "DELETE FROM contrato_persona WHERE idPersona=%s"


    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratos_personas=[]
                for r in registros:
                    contrato_persona = Contrato_Persona(r[0],r[1])
                    contratos_personas.append(contrato_persona)
                return contratos_personas
    
    @classmethod
    def insertar(cls,contrato_persona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                valores = (contrato_persona._id_Persona, contrato_persona._id_Contrato)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount

if __name__ == "__main__":
    pass
    contrato_persona1 = Contrato_Persona(idPersona="1", idContrato="1")
    contrato_personaInsertadas = ContratoPersonaDao.insertar(contrato_persona1)
    log.debug(f"Registros insertados {contrato_personaInsertadas}")
    
    """contrato_persona= ContratoPersonaDao.seleccionar()
    for p in contrato_persona:
        log.debug(p) """