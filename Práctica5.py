# #5 Manejo de información
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato “{llave}”: “{Valor}”

def impllavevalor(*parametros):
    idi=1
    dic={}
    llave=""
    valor=""
    for param in parametros:
        if(idi%2==0):
            valor= param
            dic[llave] = valor
        else:
            llave = param
        idi=idi+1
    print(dic)
    
impllavevalor("Asignatura","Matematicas","Valor",2,"Condicionante", "Ninguna")
