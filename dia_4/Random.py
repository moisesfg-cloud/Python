#Random es una libreria dentro de la cual vamos a usar randit
#Desde libreria random imprta el metodo random
"""Vamos a conocer los 5 metodos de random
randint() -> Integer aleatorio
uniform() -> Aleatorio decimal / float
random() -> Aleatorio, va sin parametros y selecciona un numero decimal o entero entre 1 y 0, bueno para trabajar con fracciones
choice() -> Seleccion aleatoria dentro de los elementos de una lista
shuffle() -> Mezclar, juegos de cartas es util
"""
from random import *

aleatorio = randint(1,90)
print(aleatorio)

print("<------------------------>")

aleatorio = round(uniform(10,40),2) # Para que no nos de tantos decimales, usamos el metodo redondeo para escoger cuantos decimales queremos
print(aleatorio)

print("<------------------------>")
# Brinda fracciones de un entero, es decir que no pasa del 0.9
aleatorio = random()
print(aleatorio)

print("<------------------------>")
#Trabaja con los elementos que esten dentro de una lista y hace una seleccion de manera aleatoria
colores = ['azul','verde','amarillo','rojo']
aleatorio = choice(colores)
print(aleatorio)

print("<------------------------>")
# Realiza una mezcla de los numeros dentro de la lista y que avanza de 5 en 5 segun el 3er parametro
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)