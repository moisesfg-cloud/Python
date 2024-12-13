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

from Proyectos_chatgpt import numeros
from dia_4.Rango import lista

aleatorio = randint(1,90)
print(aleatorio)

aleatorio = round(uniform(1,40),2) # Para que no nos de tantos decimales, usamos el metodo redondeo para escoger cuantos decimales queremos
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul','verde','amarillo','rojo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)