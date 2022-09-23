###2 Manejo y manipulación de elementos de una lista
##Escribir un programa que almacene el abecedario en una lista
#Hacer lista
lista = []
#Que almacene el abecedario
for letra in range(ord('a'),ord('z')+1):
    lista.append(chr(letra))
##elimine de la lista las letras que ocupen posiciones múltiplos de 3
i = 1
listaremo = []
for le in lista:
    if(i%3==0):
        listaremo.append(le)
    i = i+1
for le in listaremo:
    lista.remove(le)
##muestre por pantalla la lista resultante.
print(lista)