# ##3 Entrada de datos y manipulación.
# #Escribir un programa que permita al usuario capturar su nombre completo
nombrecompleto = input()
# e imprima su nombre de manera inversa letra por letra
nombrealreves=[]
for letra in nombrecompleto:
    nombrealreves.append(letra)
nombrealreves.reverse()

for letra in nombrealreves:
    print(letra)