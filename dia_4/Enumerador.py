#Nos permite enumerar
"""lista = list(enumerate(range(1,10)))
print(lista)
"""
from email.mime.audio import MIMEAudio
from operator import index

lista = ['a','b','c']
indice = 0
for i in lista:
    print(indice,lista)
    indice +=1

#Otra manera de hacerlo
lista = ['a','b','c']
for i in enumerate(lista): #Por cada item en lista enumeralos
    print(i) # Imprimimos item

#Como ingresar a los tuples
lista = ['a','b','c']

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0]) #Aquí estamos solicitando imprimir el indice 1 con el valor 0

print("<----------------->")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,i in enumerate(lista_nombres):
    print(f"{i} se encuentra en el  índice {indice}")

print("<----------------->")

cadena = "Python"
lista_indices = list(enumerate(cadena))
print(lista_indices)

print("<----------------->")

lista_nombre = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombre):
    if nombre.startswith("M"):
        print(indice)