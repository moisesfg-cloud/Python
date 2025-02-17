from random import *
nombre = input("Ingresa tu nombre: ").capitalize()
print(f"""Bueno, {nombre} he pensado un número entre 1 y 100, 
y tienes solo ocho intentos para adivinar cuál crees que es el número""")
numero_secreto = randint(0,100)
intentos = 8
print(numero_secreto)
while intentos > 0:
    intentos -=1
    numero_usuario = int(input("Ingresa el numero a adivinar: "))
    print(f"Te quedan {intentos} intentos")
    if numero_usuario == numero_secreto:
        print(f"Adivinaste el número, te quedaron {intentos} intentos")
        break
    elif numero_usuario not in range(0,100):
        print("Has elegido un número fuera del rango")
    elif numero_usuario < numero_secreto:
        print("El numero que ingresaste es menor")
    elif numero_usuario > numero_secreto:
        print("El numero que ingresaste es mayor")

