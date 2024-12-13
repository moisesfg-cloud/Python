#Python las hace en automatico: convierte el tipo de datos en otro tipo de dato automáticamente y el usuario no debera hacer nada

"""num1  = 5.8 #Asignamos un valor a la variable
print(num1) #Imprimimos la variable
print(type(num1)) #Se imprime el tipo de variable
num2 = int(num1) #Se hace la conversion para que el valor de la variable sea igual a un integer.
print(num2) #Se imprime el nuevo valor de "num2"
print(type(num2)) #Imprimimos el tipo de dato que ahora pertenece a "num2"
"""

entero = 15 #Brindar un valor a la variable
flotante = 32.2 #Brindar un valor a la variable
resutlado = entero + flotante #Se reaiza la suma de variables mediante otra variable y python hace la conversion en automatico
print(f"El resultado de la opeacion es igual a: {resutlado}") # Se imprime el valor de la variable en la cual se realiza la operacion
print(type(entero))
print(type(flotante))
print(type(resutlado)) #Imprimimos el tipo de valor de la variable

print("<--------------------------->")

texto = "El respuesta es: " #Agregamos una cadena de # texto dentro de la variable
numero = 23 #Otorgamos un valor a la variable
resultado = texto + str(numero) #Se realiza la concatenacion de un string con un integer dentro de la suma se hace la conversion para que el integer pase como string
print(resultado) #Se imprime el resultado
print(type(texto))
print(type(numero))
print(type(resutlado))

print("<--------------------------->")

numeros = [10,20,30,40,50,60]  # Lista de números enteros
suma = sum(numeros)  # Sumar los números de la lista
promedio = suma / len(numeros)  # Calcular el promedio, asegurándose de que el resultado sea un número flotante
print(f"El promedio es: {promedio}")# Imprimir el resultado
print(type(numeros))
print(type(promedio))

print("<--------------------------->")