
print("Calculadora de Comisiones")
Nombre = input("Ingresa tu nombre: ").upper()
comision = float(input("Ingresa el monto de tus ventas totales: "))
operacion = round(comision*13/100,2)
print(f"{Nombre} vendiste ${comision} por lo cual tu comision es igual a: ${operacion}")