from random import *
palabra = ["Carro","vava","papoi"]
azar = choice(palabra).lower()
largo = len(azar)
guiones = list("_" * largo)
lista_error = []
print(f'La palabra contiene {largo} letras')
print(guiones)
vidas =5
while  vidas in range(1,6):
    ingreso = str(input("Ingresa una letra: "))
    if ingreso in azar:
        for i in azar:
            indice = azar.index(ingreso, 0)
            guiones[indice] = ingreso
            break
        for j in azar:
            indice = azar.rindex(ingreso, 0)
            guiones[indice] = ingreso
            print(guiones)
            break
    elif ingreso not in azar:
        lista_error.append(ingreso)
        print(f"La letra {ingreso} no se encuentra en {guiones}")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
        print("Las letras incorrectas son:",lista_error)
    elif ingreso is not str:
        vidas -= 1
        print("Caracter no valido")
        print(f"Te quedan {vidas} vidas")
    if "_" not in guiones:
        print("FELICIDADES, Adivinaste la palabra!! ")
        break