from PersonaDao import PersonaDao, Persona
from ContratoDao import ContratoDao, Contrato
from ContratoPersonaDao import ContratoPersonaDao, Contrato_Persona

Op1 = int(input(print("Seleccione la tabla que desea utilizar: \n1. Personas \n2. Contratos \n3. Contrato Persona")))
if Op1 == 1:
    Op2 = int(input("Seleccione la operacion a realizar \n "+"1.Insertar \n 2.Seleccionar \n 3.Actualizar \n 4.Eliminar\n: \n"))
    if Op2 == 1:
        InsertarPersona = Persona(input("Ingrese los datos: "))
        Inserts = PersonaDao.insertar(InsertarPersona)
        print("Registro correctamente")
    if Op2 == 2:
        InsertarPersona = tuple(input("Ingrese el id de la Persona: "))
    if Op2 == 3:
        InsertarPersona = tuple(input("Ingrese los datos: "))
    if Op2 == 4:
        InsertarPersona = tuple(input("Ingrese los datos: "))
elif Op1 == 2:
    Op2 = int(input("Seleccione la operacion a realizar \n "+"1.Insertar \n 2.Seleccionar \n 3.Actualizar \n 4.Eliminar\n: \n"))


print("Seleccione la tabla que desea utilizar: ")