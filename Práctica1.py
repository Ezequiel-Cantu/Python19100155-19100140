#Practica 1
#### 1 Funciones con n parámetros
##Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total.
def productotal(*parametro):
    prodtota = 1
    for number in parametro:
        prodtota = number * prodtota
    print(prodtota)
    

##Imprimir
productotal(3,4,5,3)