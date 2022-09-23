# #4 Entrada de datos y estructuración.
# Revisar su retícula 
# para escribir un programa que cree un diccionario vacío 
# para que el usuario capture las materias y créditos de su semestre preferido (inferior a 8vo) 
# al final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. 
# Y la suma de todos los créditos del semestre.

from hashlib import new

asigdic = {}
print("¿Cual es su semestre favorito?")
semfav = input()

for i in range(9):
    print("Inserte Asignatura")
    asig = input()
    print("Inserte creditos")
    cred = int(input())
    print("¿Desea continuar? Y / N")
    dec = (input())
    asigdic[asig] = cred
    if(dec == "n" or dec == "N"):
        break

credtot=0

for cred in asigdic:
    print(cred + " tiene " + str(asigdic[cred]) + " creditos.")
    credtot = credtot+ asigdic[cred]

print("Sus creditos totales son: ")
print(credtot)