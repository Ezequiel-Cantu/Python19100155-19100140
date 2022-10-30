from persona import Bailarin
from Conexion import Conexion
from logger_base import log
from psycopg2 import pool

class PersonaDao:
    _SELECCIONAR = "SELECT * FROM bailarin ORDER BY id_bailarin"
    _INSERTAR = "INSERT INTO bailarin(nombre,apellido,danza,nivel) Values(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE bailarin SET nombre=%s,apellido=%s,danza=%s,nivel=%s WHERE id_bailarin = %s"
    _ELIMINAR = "DELETE FROM bailarin WHERE id_bailarin=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                bailarines=[]
                for r in registros:
                    bailarin = Bailarin(r[0],r[1],r[2],r[3],r[4])
                    bailarines.append(bailarin)
                return bailarines
    
    @classmethod
    def insertar(cls,bailarin):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                valores = (bailarin._nombre, bailarin._apellido, bailarin._danza, bailarin._nivel)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount

    @classmethod
    def actualizar(cls,bailarin):
       with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
             valores = (bailarin._nombre,bailarin._apellido, bailarin._danza, bailarin._nivel,bailarin._id_bailarin)
             cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,bailarin):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
             valores = (bailarin._id_bailarin,)
             cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount

if __name__ == "__main__":
    
    persona1 = Bailarin(nombre="Aquiles",apellido="Cantu",danza="Jazz y Ballet",nivel="Avanzado")
    personasInsertadas = PersonaDao.insertar(persona1)
    log.debug(f"Bailarines insertadas {personasInsertadas}")
    
    persona1 = Bailarin(id_bailarin=1,nombre="Ezequiel",apellido="Cantu",danza="Ballet",nivel="Avanzado")
    personasActualizadas = PersonaDao.actualizar(persona1)
    log.debug(f"Bailarines actualizadas {personasActualizadas}")
    
    persona1 = Bailarin(id_bailarin=5)
    personasEliminadas = PersonaDao.eliminar(persona1)
    log.debug(f"Bailarines eliminadas {personasEliminadas}")
   
    bailarines = PersonaDao.seleccionar()
    for b in bailarines:
        log.debug(b)