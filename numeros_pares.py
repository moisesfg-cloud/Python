"""Números pares e impares
Pide al usuario un número y muestra todos los números desde 1 hasta ese número, indicando si cada uno es par o impar."""
numero_usuario = int(input("Ingresa un número: "))
for i in range(1,numero_usuario +1):
    if i % 2 == 0:
        print(f"El número {i} es par")
    if i % 2 == 1:
        print(f"El número {i} es impar")
