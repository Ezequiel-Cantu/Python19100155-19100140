# #7 Formateo y conversiones
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha del día de hoy en el formato seleccionado.
from datetime import date
print("1.- Imprimir YYYY/MM/DD    " + "“2.- Imprimir MM/DD/YYYY”")
decision = input()
if (decision == "1"):
    fecha = date.today()
    print(str(fecha.year) + "/" + str(fecha.month) + "/" + str(fecha.day))
elif(decision=="2"):
    fecha = date.today()
    print(str(fecha.month)+"/"+str(fecha.day)+"/"+str(fecha.year))
