#upper() - pasar a mayusuclas
#lower() - pasar a minusculas
#split() - separalo en partes (lista)
#join() - unir items usando separador
#find() - encontrar un sub-string
#replace() - reemplazar un substring
#son mas de 30 metodos, los metodos todos llevan parentesis
print("<----------->\n")

print("UPPER")#De esta manera logramos convertir el texto completo en mayusculas
texto = "Este es el texto de Moises"
resultado = texto.upper()
print(resultado)

#Si solo quieres que una letra sea la que se ve en minuscula deberas escribir el codigo de esta manera:
texto = "Este es el texto de Moises"
resultado = texto[1].upper()
print(resultado)

print("<----------->\n")

print("LOWER") #De esta manera logramos convertir el texto completo en minusculas
texto = "Este es el texto de Moises"
resultado = texto.lower()
print(resultado)
#Si solo quieres que una letra sea la que se ve en minuscula deberas escribir el codigo de esta manera:
resultado = texto[2].lower()
print(resultado)

print("<----------->\n")

print("SPLIT") #Lo que hace split es separar el texto y convertirlo en una lista toma como separador los espacios que hay entre palabras

texto = "Esta sera una lista".lower()
resultado = texto.split("e") #Esta e dentro de los parentesis hara que split comience a separar el texto en donde se encuentren las letras "e"
print(resultado)

texto = "Este es el texto de Moises"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Moises"
resultado = texto.split("t") #Si ponemos entre comillas y dentro de los parentesis una letra ahora split
# tomara como separador a la letra que ingresamos por lo cual cada vez que haya una palabra que la contenga se separara
print(resultado)


print("<----------->\n")

print("JOIN") #join se encarga de unir variables, las cuales deberan de estar dentro de una lista
#En este ejercicio vamos a ver como se unen mediante el metodo join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #Aquí mediante la funcion de .join vamos a unir las variables, cabe mencionar que debemos de hacer una lista dentro del metodo para poder indicar que variables se van a utilizar
print(e)

a = "Hola"
b = "Moises"
c = " ".join([a,b])
print(c)

print("<----------->\n")

print("FIND") #Busca caracteres en especifico y te brinda el indice desde el cual comienza, cuando find no encuentra lo que buscas siempre regresara un resultado con -1
texto = "Este es el texto de Moises"
resultado = texto.find("texto")
print(resultado)


print("<----------->\n")


print("REPLACE") #De esta manera se puede hacer el remplazo de una cadena de texto
texto = "Este es el texto de Moises"
resultado = texto.replace("Moises","CR7")#El primer parametro es el texto viejo y separado de una coma el texto nuevo o de reemplazo
print(resultado)

