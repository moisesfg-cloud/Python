

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = 0 #Variable para contar los numeros pares
for i in numeros: #Recorremos la lista de numeros con el bucle for
 if i % 2 == 0:
  numeros_pares +=1  #Si es par, aumentara el contador
print(f"La cantidad de úmeros pares es: {numeros_pares}")

