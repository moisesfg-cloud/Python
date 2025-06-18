
palabra = "python"
lista = []
for i in palabra:
    lista.append(i)
print(lista)

print("<------------------->")

#Comprension de listas
palabra = "python"
lista = [i for i in palabra] #Item por item dentro de poalabra, crea una lista
print(lista)

print("<------------------->")
#Con solo un string puedes crear la lista
lista = [i for i in "python"]
print(lista)

print("<------------------->")
#Numero por numero dentro del rango de 1 al 40 cada 2 numeros
lista = [n for n in range(1,40,2)]
print(lista)

print("<------------------->")
#Numero por numero dentro del rango de 1 al 40 cada 2 numeros pero dividido por dos
lista = [i/2 for i in range(1,40,2)]
print(lista)

print("<------------------->")
#Aqui el item que sea mayor al 10 dentro del rango
lista = [i for i in range(1,10,2) if i *2 >10]
print(lista)

print("<------------------->")
#Si usamos else dentro de la lista debe de ir despues de la priemra variable
#Dentro de la lista y el rango del 1 al 10 cada 2 numeros numeros que sean menores a 10 se contestara con un 10
lista = [i if i *2 >10 else "NO" for i in range(1,10,2)]
print(lista)

print("<------------------->")

#pasar de pies a metros
pies = [10,20,30,40,50]
metros = [i /3.281 for i in pies]
print(metros)

print("<------------------->")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [i **2 for i in valores]
print(valores_cuadrado)

print("<------------------->")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [i for i in valores if i % 2 == 0]
print(valores_pares)

print("<------------------->")

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(i-32)*(5/9) for i in temperatura_fahrenheit  ]
print(grados_celsius)








