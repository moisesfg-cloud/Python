#round (redondeo)
# sintaxis round(parametro1, parametro2) párametro1 = numero, operacion, variables o funciones; párametro2 = consiste en informar cuantos numeros decimales queremos
#redondea segun el numero mas cercano 5.3 = 5, 5.8= 6 y de 5.5 redondea hacia arriba = 6

#  Parametro1  ___ Parametro2 cuantos decimales queremos, se pueden colocar numeros, operaciones, variables, funciones
#           |  |
print(round(9.7))

num1 = round(90/7,1)
print(num1)
#<---------------------------------------->
valor = round(95.66666666) #Marcara que es un integer ya que al momento de redondear recordemos que decimales arriba de .5 el valor incrementa y se esta redondeando desde el comienzo y dentro de la variable
print(valor)
print(type(valor))
#<---------------------------------------->

valor = 95.66666666 #Marcara que es un float debido a que el round se esta llevando acabo fuera de la variable
print(round(valor))
print(type(valor))
print(valor)
print(type(valor))

#Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
#Como lo hice antes:
valor1 = 10
valor2 = 3
operacion = round(10/3,2)
#<---------------------------------------->

#Como lo hago ahora:
print(round(10/3,2))
