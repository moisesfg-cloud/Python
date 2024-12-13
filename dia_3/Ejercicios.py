from random import random, randint
from re import split

texto = "Hola, mundo!"
texto_modificado = texto.replace("o", "a")
print(texto_modificado)


"""#REPLACE
texto =  "Hola mundo, el mundo es bonito."
Palabra_a_reemplazar =  "mundo"
Nueva_palabra = "planeta"
modificacion = texto.replace("mundo","planeta")
print(modificacion)

#FIND
cadena = input("Ingresa una cadena: ")
palabra = input("Ingresa una palabra: ")
print(f"La aparicion de la palabra comienza en {cadena.find(palabra)}")"""

"""#JOIN
ingreso_letras = input("Ingresa una lista de palabras separadas: ")
print(ingreso_letras)
lista = ingreso_letras.split()
print(lista)
union = " ".join(lista)
print(union)

#SPLIT
ingreso_letras = input("Ingresa una lista de palabras separadas: ")
lista = ingreso_letras.split()
print(lista)"""

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
reemplazo = (texto.replace("difícil","facil").replace("mala","buena"))
print(reemplazo)

#Este es un ejercicio para sobrescribir los valores dentro de las listas
lista = ['a','b','c'] #Creamos listas con valores
lista [0] = "alfa" #Ingresamos entre corchetes el numero de indice a sobreescirbir y atraves de signos de igual y comillas establecemos el nuevo valor
print(lista) #Imprimimos la salida del nuevo valor dentro de la lista
print(lista)

ingreso = int(input("Ingresa el precio del producto: $"))
iva = ingreso * 21 /100
print(f"El precio de tu producto con iva seria de ${iva + ingreso}")

{ yhge}
print(rango)
for i in rango:
    if i %2 == 1:
        print(i /2)

