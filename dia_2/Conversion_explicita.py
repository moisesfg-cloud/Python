#python necesita que el usuario haga algo para convertir un tipo de dato en otro.

edad = input ("Ingresa tu edad: ") #Solicitamos al usuario que ingrese su edad,
edad = int(edad) #Se hace la conversion de string (texto) a integer (número)
print(edad) #Imprimimos el resultado de edad
print(type(edad)) #Imprimimos el tipo de dato que se tiene en la variable "edad"
nueva_edad  = 1 + edad
print(f"Tu nueva edad es: {nueva_edad}" )

#<---------------------------------------->


cadena = "100.5" # Tipo str
# Convertir explícitamente la cadena a un número flotante
numero_flotante = float(cadena)# Convertir el número flotante a entero explícitamente (pierde la parte decimal)
numero_entero = int(numero_flotante) #Conversion de float a int
print(f"El número flotante es igual a: {numero_flotante}")
print(f"El núero entero es igual a: {numero_entero}")

#<---------------------------------------->

# Número entero
numero = 100
# Convertir el número a cadena
cadena_numero = str(numero)
# Imprimir el resultado
print(f"El número entero {numero} convertido a cadena es: '{cadena_numero}'")

#<---------------------------------------->


num1 = "7.5" #str
num2 = "10" #str
# Conversion de str a float dentro de un print
print(float(num1)+float(num2))


