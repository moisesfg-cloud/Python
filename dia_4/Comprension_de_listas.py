
palabra = "python"

lista = []
for i in palabra:
    lista.append(i)
print(lista)

#Comprension de listas
palabra = "python"
lista = [i for i in palabra]
print(lista)

lista = [i for i in "python"]
print(lista)



lista = [n for n in range(1,40,2)]
print(lista)

lista = [i/2 for i in range(1,40,2)]
print(lista)

lista = [i for i in range(1,10,2) if i *2 >10] #Esto va de esta manera siempre y cuando solo se use el if
print(lista)


lista = [i if i *2 >10 else "NO" for i in range(1,10,2)] #Si usamos else dentro de la lista debe de ir despues de la priemra variable
print(lista)



#pasar de pies a metros
pies = [10,20,30,40,50]
metros = [i /3.281 for i in pies]
print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [i **2 for i in valores]
print(valores_cuadrado)



valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [i for i in valores if i % 2 == 0]
print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(i-32)*(5/9) for i in temperatura_fahrenheit  ]
print(grados_celsius)








