print("Hola, el día de hoy te ayudare a calcular tu comision")
nombre = input('Ingresa tu nombre: ')
ventas = input("Ingresa tus ventas de este mes: ")
comisiones = float(ventas)
calculo = comisiones * 13 /100
print(nombre, "tus comisiones de este mes son: $", calculo ,"peso")
