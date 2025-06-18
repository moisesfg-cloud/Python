from random import *

nombre = input("Cual es tu nombre: ")
numero_random =randint(0,100) #Genera el número random
intentos = 8
print(f"Bueno {nombre} he pensado un número entre el 1 y el 100")
print(numero_random)
while intentos >1:
    intentos -=1
    numero_usuario = int(input("Ingresa el número que crees correcto: "))
    print(f"Te quedan {intentos} intentos")
    if (numero_usuario > 100 or numero_usuario < 0):
        print("Número no permitido")
    if (numero_usuario < numero_random):
        print("Respuesta incorrecta, el número es mayor")
    if (numero_usuario > numero_random):
        print("Respuesta incorrecta, el número es menor")
    if (numero_usuario == numero_random):
        print(f"Felicidades has acertado, te quedaron {intentos} intentos")
        break
