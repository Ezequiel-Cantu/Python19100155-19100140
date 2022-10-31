from Contrato import Contrato
from Conexion import Conexion
from logger_base import log
from psycopg2 import pool

class ContratoDao:
    _SELECCIONAR = "SELECT * FROM contrato"
    _INSERTAR = "INSERT INTO contrato(\"noContrato\",costo,\"fechaInicio\",\"fechaFin\") Values(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE contrato SET noContrato= %s,costo= %s,fechaInicio= %s,fechaFin= %s WHERE idContrato = %s"
    _ELIMINAR = "DELETE FROM contrato WHERE idContrato=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratos=[]
                for r in registros:
                    contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                    contratos.append(contrato)
                return contratos
    
    @classmethod
    def insertar(cls,contrato):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
                valores = (contrato._noContrato,contrato._costo,contrato._fechaInicio, contrato._fechaFin)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount

    @classmethod
    def actualizar(cls,contrato):
       with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
             valores = (contrato._noContrato,contrato._costo,contrato._fechaInicio, contrato._fechaFin,contrato._id_Contrato)
             cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,contrato):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor()as cursor:
             valores = (contrato._id_Contrato,)
             cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        

if __name__ == "__main__":
    
    contrato1 = Contrato(noContrato=19100155,costo= 2540.5,fechaInicio= "21/08/22",fechaFin= "31/10/22")
    contratosInsertados = ContratoDao.insertar(contrato1)
    log.debug(f"Contratos insertados {contratosInsertados}")
    
    contratos= ContratoDao.seleccionar()
    for c in contratos:
        log.debug(c)