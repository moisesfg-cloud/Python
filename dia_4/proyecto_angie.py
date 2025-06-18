from random import *
inf= 0
sup= 100
aleatorio=randint(inf,sup)
intentos= 0
i = None #Número de usuario
while intentos >=8:
    while i != aleatorio: #Mientras i sea diferente a aleatorio se ejecutara todo
        intentos = intentos+1
        print("El numero esta entre ", inf, " y " ,sup)
        i=int(input("Adivina el numero: "))
        if i < aleatorio and i>inf:
            inf=i
        elif i>aleatorio and i<sup:
            sup=i
        if i==aleatorio:
            print("FELICIDADES, adivinaste en ", intentos," intentos")
            break

