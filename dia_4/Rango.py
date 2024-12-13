#Evitamos estar creando listas

"""rango = range (9)
for  i in rango:
    print(i)"""

for i in range(1,5): # El primer parametro nos idica desde donde comenzara y el segundo hasta donde termina el rango y un tercer rango en caso de ser agregado indica cada cuantos numeros se considerarar
    print(i)


lista = list(range(1,101))
print(lista)

print("<-------------------_>")

"""Práctica Rango 3
Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
Para ello:
Crea un rango de valores que puedas recorrer en un loop
Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados."""

suma_cuadrados = 0
for i in range(0,16):
    suma_cuadrados = suma_cuadrados + i**2
    print(suma_cuadrados)