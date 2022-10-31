from Persona import Persona
from Conexion import Conexion
from logger_base import log
from psycopg2 import pool

class PersonaDao:
    _SELECCIONAR = "SELECT * FROM persona"
    _INSERTAR = "INSERT INTO persona(nombre,edad,correo) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s,edad=%s,correo=%s WHERE idPersona = %s"
    _ELIMINAR = "DELETE FROM persona WHERE idPersona=%s"
    _SUMA = "SELECT SUM(c.costo) FROM contrato_persona cp JOIN contrato c on cp.\"idContrato\" = c.\"idContrato\" JOIN persona p on cp.\"idPersona\" = p.\"idPersona\" WHERE p.correo = %s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas=[]
                for r in registros:
                    persona = Persona(r[0],r[1],r[2],r[3])
                    personas.append(persona)
                return personas
    
    @classmethod
    def insertar(cls,persona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                valores = (persona._nombre, persona._edad, persona._correo)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
       with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
             valores = (persona._nombre, persona._edad, persona._correo,persona._id_persona)
             cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
             valores = (persona._id_persona,)
             cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
    
    @classmethod
    def Suma(cls,persona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                valores = (persona._correo,)
                cursor.execute(cls._SUMA,valores)
                return cursor.rowcount
        

if __name__ == "__main__":
    
    persona1 = Persona(nombre="Carlos",edad=29,correo="ezequielcantu_19@hotmail.com")
    personasInsertadas = PersonaDao.insertar(persona1)
    log.debug(f"Personas insertadas {personasInsertadas}")
    
    suma1 = PersonaDao.Suma(persona1)
    log.debug(f"Suma {suma1}")
    
    personas= PersonaDao.seleccionar()
    for p in personas:
        log.debug(p)