#Importamos la libreria random para usar shuffle
import random
from os import remove
from random import *
from xml.sax.handler import property_interning_dict

# lista incial

#Creamos una variable con el nombre de "palitos" la cual contiene una lista con longitiudes distintas.

palitos = ['-','--','---','----']
# mezclar palitos

#Creamos una funcion que se llame mezclar palitos la cual mediante shuffle se realice el cambio aleatorio y que al mismo tiempo
#nos retorne la lista con los cambios

def mezclar(lista):
    shuffle(lista)
    return lista
print(mezclar(palitos))
# pedirle intento
def probar_suerte():
    intento = ' '

    while intento not in ['1','2','3','4']: #Mientras intento no este en la lista del 1 al 4
        intento = input ("Eliege   un  lnumero del 1 al 4: ")

    return int(intento)

# Comprobar intento
def chequear_intento(lista, intento):
    if lista [intento -1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
print("<------------------------------------------_>")


#Nuevo ejercicio
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)

def evaluar_jugada(valor1,valor2): #Recibe dos argunmentos
    suma_dados = valor1 + valor2
    if suma_dados <=6:
        return(f"La suma de tus dados es {suma_dados}. "
                f"Lamentable")
    if suma_dados > 6 and suma_dados < 10:
        return (f"La suma de tus dados es {suma_dados}."
                f"Tienes buenas chances")
    if suma_dados >= 10:
        return (f"La suma de tus dados es {suma_dados}."
                f"Parece una jugada ganadora")
    print(evaluar_jugada(valor1,valor2))

print("<------------------------>")

#Ejercicio 2

lista_numeros = [1,3,2,4,5,1,2,3,12,4,5,2,30]
def reducir_lista(lista):
    # Se eliminan los numeros duplicados
    lista_sin_duplicados = set(lista)
    # Elimina el valor mayor
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados
nueva_lista = reducir_lista(lista_numeros)
print(nueva_lista) #Imprime la lista con los parametros que se especifican dentro de la funcion
def promedio(lista):
    return sum(lista)/len(lista)
print(f"El promedio de la lista es: " + str(promedio(nueva_lista)))

print("""
#╔═╗┌┐┌┌─┐┬┌─┐
#╠═╣││││ ┬│├┤
#╩ ╩┘└┘└─┘┴└─┘
""")
lista_numeros=[1,2,15,7,2,7]
def reducir_lista(parametro):
    lista_sin_dup=list(set(parametro))
    lista_ordenado=sorted(lista_sin_dup)
    lista_ordenado.pop(len(lista_ordenado)-1)
    return lista_ordenado
nueva_lista=reducir_lista(lista_numeros)
print(nueva_lista)
def promedio(parametro):
    return sum(parametro)/len(parametro)
print(promedio(nueva_lista))

#Ejercicio 3
lista_numeros = [1,2,3,4,5,6]

def lanzar_moneda():
    opcion = ["Cara","Cruz"]
    azar = choice(opcion)
    return azar
print(lanzar_moneda())

def probar_suerte(moneda,lista):
    if moneda == "Cara":
        print("La lista se autodestruira")
        return []
    if moneda == "Cruz":
        print("La lista fue salvada")
        return lista
print(probar_suerte(lanzar_moneda(),lista_numeros))