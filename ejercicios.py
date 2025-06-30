"""from random import *
valor1 = opcion = choice(["cara","cruz"])
print(valor1)
valor2 = [1,2,3,4,5,6]
if valor1 == "cara":
    print("La lista se autodestruira")
    valor2.clear()
    print(valor2)
if valor1 == "cruz":
    print("La lista fue salvada")
    print(valor2)

"""
import random


#EJERCICIOS FUNCIONES

def saludo():
    print("Hola amiga")
saludo()

#Escribir una función que reciba un número entero positivo y devuelva su factorial
lista_numeros = [1, 2, 3, 4, 5, 6]

def lanzar_moneda():
    opcion = random.choice(["cara", "cruz"])
    return opcion

def probar_suerte(moneda, lista):
    if moneda == "cara":
        print("La lista se autodestruira")
        return lista.clear
    print(lista)

    if moneda == "cruz":
        print("La lista fue salvada")
        return lista
    print(lista)

