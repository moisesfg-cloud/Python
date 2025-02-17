
lista_numeros=[10,20,30,40,50]
def suma_menores(lista_numeros):
    suma = 0
    for i in lista_numeros: #leer numeros
        if i in range(10,100):
            suma += i #Va a sumar el i por si mismo
        else:
            pass
    return suma
resultado = suma_menores(lista_numeros)
print(resultado)

lista_numeros= [2,4,6,7,8]
def cantidad_pares(lista_numeros):
    numeros_pares = 0
    for i in lista_numeros:
        if i % 2 == 0:
            numeros_pares += 1
        else:
            pass
    return numeros_pares
resultado = cantidad_pares(lista_numeros)
print(resultado)

