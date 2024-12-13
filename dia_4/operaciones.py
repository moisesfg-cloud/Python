lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0
for i in lista_numeros:
    if i  % 2 == 0:  #Si el numero dividido a 2 es igual a 0 es par porque no tiene residuo
        suma_pares = suma_pares + i #Se procede a hacer la suma de numeros pares
print(f"La suma de los números pares es {suma_pares}")
        #print(f"Estos son numeros pares {i}" )
for i in lista_numeros:
    if i % 2 ==1: #Si el numero divido a 2 es igual a 1 es par porque tiene residuo
     suma_impares = suma_impares + i #Se procede a hacer la suma de numeros impares
print(f"La suma de los números impares es: {suma_impares}")
        #print(f"Estos son numeros impares {i}" )
