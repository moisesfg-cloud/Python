"""Pide al usuario que ingrese 5 nombres y almacénalos en una lista. Luego, muestra la lista en orden inverso y en orden alfabético."""
lista_nombres = []
lista_nombres.append(input("Ingresa el primer nombre: "))
lista_nombres.append(input("Ingresa el segundo nombre: "))
lista_nombres.append(input("Ingresa el tercer nombre: "))
lista_nombres.append(input("Ingresa el cuarto nombre: "))
lista_nombres.append(input("Ingresa el quinto nombre: "))
lista_nombres.reverse()
print(lista_nombres)
lista_nombres.sort()
print(lista_nombres)