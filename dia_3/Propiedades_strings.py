"""Los string son inmutables, una vez que han sido construidos no puedes cambiar su orden
ni su contenido.
Se pueden concatenar, multiplicar entre otras
Se puede tener mas de una linea con mas de tres comillas dobles """

nombre = "Carina"



n1 = "Kari"
n2 = "na"
print(n1 + n2)

n1 = "Kari"
n2 = "na"
print(n1 * 10) #De esta manera repetimos 10 veces

poema = """Mil pequeños peces blancos
comon si hirviera
el color del agua"""
print("sol" in poema) #De esta manera preguntamos si el texto esta dentro de la variable
print("sol" not in poema) #De esta manera preguntamos si el texto no esta dentro de la variable

print("LEN")
# Len es el largo del texto, ya sean numeros,letras etc...
print(len(poema))
