#Cuando hay un (in) es una comparacion boolena
#Este bloque lo hace es recibir un parametro numerico y mediante un for y range valida si el parametro numerico tiene 3 cifras


def revisar(numero):
     return numero in range(100,1000)
"""Lo que estamos presenciando es, poder analizar un numero
si es que cuenta con 3 cifras o no"""
resultado =  revisar(100)
print(resultado)

def revision_3_cifras(numero):
    return numero in range(100,1000)
suma = 586 + 402
resultado = revision_3_cifras(suma)
print(resultado)



def revision_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return  True
        else:
            pass #Con este "pass" lo que sucede es que recorre cada valor de la lisrta hasta validar si alguno cumple
        return False
resultado = revision_3_cifras([55,99,4000])
print(resultado)


def revision_3_cifras(lista):
    lista_vacia = []
    for n in lista:
        if n in range(100,1000):
             lista_vacia.append(n) #Agrega dentro de lista vacia cada item de la lista
        else:
            pass #Con este pass lo que hace es que cuando valida el 55 y no es de 3 cifras el pass hace que continue al siguiente valor
    return lista_vacia
resultado = revision_3_cifras([55,790,99,6000,200,400])
print(resultado)


lista_numeros = [10,50,-40,-10]
def todos_positivos(lista_numeros):
    for i in lista_numeros:
        if i < 0:
            return False
        else:
            pass
    return True
resultado = todos_positivos(lista_numeros)
print(resultado)

lista_numeros = [10,10,50,1,5,1200,20]

def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(10,1000):
            suma += numero
        else:
            pass
    return suma
resultado = suma_menores(lista_numeros)
print(resultado)

lista_numeros = [1, 50, 500, 5000, 750, 600]


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma

lista_numeros = [7,6,1,4,5]
def cantidad_pares(lista_numeros):
    pares= 0
    for numero in lista_numeros:
        if numero % 2 == 0:
          pares = pares + numero
        else:
            pass
    return pares
restultado = cantidad_pares(lista_numeros)
print(restultado)
