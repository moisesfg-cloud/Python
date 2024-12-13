#slicing, rebanar o exraer identificar en que indice se ecuentra cada caracteres

texto = "ABCDEFG"
extraer = texto[1:7] #De esta manera se extraen los caracteres desde el cual se indica con los numeros
print(extraer)

print("<----------->\n")
texto = "ABCDEFG"
extraer = texto[1] #De esta manera extraes el simbolo que se encuentra en la posicion indicada
print(extraer)

print("<----------->\n")
texto = "ABCDEFG"
extraer = texto[1:9] #De esta manera se extraen los caracteres desde el cual se indica con los numeros
print(extraer)

print("<----------->\n")
texto = "ABCDEFG"
extraer = texto[1:] #De esta manera se extraen todos los simbolos comenzando desde el mumero indicado
print(extraer)

print("<----------->\n")
texto = "ABCDEFGHIJKLM"
extraer = texto[0:9:2] # De esta manera se van a extraer todas todos los caracteres indicados por posicion, de dos en dosb el ultimo numero indica con saltos de cuantos parametros se extraen datos
print(extraer)

print("<----------->\n")
texto = "ABCDEFGHIJKLM"
extraer = texto[::2] # De esta manera se van a extraer todos los caracteres de dos en dos
print(extraer)

print("<----------->\n")
texto = "ABCDEFGHIJKLM"
extraer = texto[::-1] # De esta manera se van a mostrar todos los carcateres de manera inversa
print("<----------->\n")

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
texto = frase[::-1]
print(texto)

nombre = "Moises"
print(nombre[0:4:2])