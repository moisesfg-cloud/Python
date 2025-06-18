#*args sirve para que el usuario no tenga limite en argumentos

def suma (a,b):
    return a+b

print(suma(5,6))

def suma (*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,6))

def suma (*args):
    return sum(args)
print(suma(5,6,6,4,32,46,43,453,))

#EJERCICIOS
print("<-------------->")
def suma_cuadrados(*args):
    total = 0
    for i in args:
        total = total +(i**2)
    return total
print(suma_cuadrados(1,2))

print("<----------------->")
def suma_absolutos(*args):
    total = 0
    for i in args:
        total = total + abs(i)
    return total
print(suma_absolutos(1,-2,-4,5))

def numeros_persona(nombre,*args):
    cantidad = sum(args)
    return f"{nombre} la suma de tus números es{cantidad}"
print(numeros_persona("moises",13,2,4,5,1,2))
