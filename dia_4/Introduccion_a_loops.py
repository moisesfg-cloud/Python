#bucle o rulo vuelva a suceder
#iterable = porque puedes repetir una repeticion por cada elemento de la lista hasta que la lista se agote
# la i es una variable interna que se ocupa solo para referirse a los elementos que existe en el objeto iterable
nombres = ['juan','moises','yair','sergio']
for i in nombres:   #La "i" representa a los elementos de la lista
    numero_de_nombre = nombres.index(i) + 1 # Quiero que comiences a contar desde uno los elementos que estan dentro de nombres
    print(f"Nombre {numero_de_nombre}: {i}")

#print("Hola" +" "+ i) #Por cada elemento que en este caso es "i" imprime "Hola" + el elemento que esta dentro de la lista
#print("Nombre : " + i)

print("<--------------------------->")


print(".STARTSWITH") #Hace la busqueda en caso de que una palabra comienza con una letra
nombres = ['juan','moises','yair','sergio']
for i in nombres:
    if i.startswith('m'): #Si el elemento comienza con la letra 'm' se imprimira
        print(i)
    else:
        print(f"Nombres que no conminezan con M: " + i)

print("<--------------------------->")

numeros = [1,2,3,4,5,]
mi_valor = 0
for i in numeros:
    mi_valor = mi_valor + i  # Esto lo que hace es lo sig: mi valor va a ser igual que mi valor osea 0, pero por cada elemento de numeros se va a it sumando por si mismo
print(mi_valor)

print("<--------------------------->")

#Tambien funciona con strings
palabra = "Python es lo mejor"
for i in palabra:
     print(i)

#O en lugar de crear una variable se puede crear en una sola linea
for i in "Palabra":
    print(i)
print("<--------------------------->")

#Con listas
for i in [1,2,3]:
    print(i)
print("<--------------------------->")

for i in [[1,2],[3,4],[5,6]]:
    print(i)

#De esta manera iteras una lista, haciendo que se imprima un elemeto de cada lista por a y b
for a,b in [[1,2],[3,4],[5,6]]:
    print(a) # 1,3,5
    print(b) # 2,4,5

print("<--------------------------->")

#Con diccionarios
dic = {'clave':'a','clave2':'b','clave3':'c'}
for concepto in dic:
    print(concepto)
#Para ver concepto y resultado
dic = {'clave':'a','clave2':'b','clave3':'c'}
for concepto in dic.items(): #De esta manera con el metodo items podremos ver toda la info
    print(concepto)


dic = {'clave':'a','clave2':'b','clave3':'c'}
for concepto in dic.values(): #De esta manera con el metodo items podremos ver los valores de cada concepto
    print(concepto)

print("<--------------------------->")

#Para ver a y b
dic = {'clave':'a','clave2':'b','clave3':'c'}
for a,b in dic.items():
    print(a,b)


print("<--------------------------->")


lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0
for i in lista_numeros:
    if i  % 2 == 0:  #Si el numero dividido a 2 es igual a 0 es par porque no tiene residuo
        suma_pares = suma_pares + i #Se procede a hacer la suma de numeros pares
print(f"La suma de los números pares es {suma_pares}")
        #print(f"Estos son numeros pares {i}" )
for i in lista_numeros:
    if i % 2 == 1: #Si el numero divido a 2 es igual a 1 es par porque tiene residuo
     suma_impares += i  #Se procede a hacer la suma de numeros impares
print(f"La suma de los números impares es: {suma_impares}")
        #print(f"Estos son numeros impares {i}" )

print("<--------------------------->")

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

rango = range(1,16)
numero = 0
for i in rango:
    numero = numero + i**2
    print(numero)

print("<--------------------------->")

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



