#Normalmente lo que se espera de las funciones es que nos puedan devolver algo
from idlelib.colorizer import prog_group_name_to_tag

from dia_2.Conversiones_implicitas import numero


def sumar(num1,num2):
 """Esta funcion esta diseñada para sumar dos valores"""
 return num1 + num2
resultado = sumar(10,20)


def multiplicar ( num1, num2):
    """
    Esta funcion multiplica los parametros
    el return nos devuelve el valor pero no se imprime, para eso hay que almacenar
    el resultado en una variable y despues imprimirla
    """
    return num1 * num2
resultado = multiplicar(10,50)
print(resultado)


def multiplicar ( numero1, numero2):
    total = numero1 * numero2
    return total
multiplicar(20,30)

def multiplicar ( numero1, numero2):
    total = numero1 * numero2
    print(total)
    return total
multiplicar(20,30)


def potencia(num1,num2):
   operacion = num1 **num2
   return operacion
potencia(3,4)

dolares = 2
def usd_a_eur(dolares):
    conversion = dolares *0.90
    print(conversion)
usd_a_eur(dolares)

dolar = 1
euro = 0.90

dolar = int(input("Ingresa cuantos dolares tienes: "))
uero = 0.90
print(f"Tienes {dolar} dolares que es equivalente a {dolar * euro} euros")


palabra = "Python"
def invertir_palabra(palabra):
 print(palabra[::-1].upper())

"""pal = "Python"
print(pal[::-1].upper())"""



palabra = "Python"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper
    return palabra
    print(palabra)


palabra = "Curso de Python"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

def sumna (num1,num2):
    return num1 + num2
resultado = sumar(5,5)
print(resultado)


def numero_mayor(x,y):
    if x > y:
        return x
    else:
        return y
valores = numero_mayor(10,40)
print(valores)

def par_o_impar(x):
    if x % 2 == 0:
        return "Par"
    else:
        return "impar"
resultado = par_o_impar(3)
print(resultado)