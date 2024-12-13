"""
if (si cumple)
elif (si no)
else (no cumple)
"""
print("<--------------------------->")

edad = 17
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("<--------------------------->")

mascota = "perro"

if mascota == "perro":
    print("Tienes un perro")
elif mascota == "gato":
    print("Tienes un gato")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No se que mascota tienes")


print("<--------------------------->")

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

print("<--------------------------->")

edad = int(input("Ingresa tu edad: "))
tiene_licencia = str(input("Tienes licencia: ")).lower()
if edad > 18:
    if tiene_licencia == "no":
        print("No puedes conducir. Necesitas contar con una licencia")
    if tiene_licencia =="si":
        print("Puedes conducir")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")


print("<--------------------------->")


"""edad = int(input("Ingresa tu edad: "))
tiene_licencia = False #No tiene
"Puedes conducir"
"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
"No puedes conducir. Necesitas contar con una licencia"
if edad > 18:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")"""

print("<--------------------------->")

habla_ingles = True #(sabe)
sabe_python = False #(no sabe)


if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")