#Nos srive para saber en que posicion se encuentra determinado caracter

texto = "Esto es una prubea"
resultado = texto[0] #De esta manera se solicita que se imprima el caracerter que esta en la posicion "0"
print(resultado)
print("<----------->\n")

mi_texto = "Esto es una prueba"
resultado = mi_texto.index("n") #De esta manera te indica el numero en el cual se encuentra el caracter
print(resultado)

print("<----------->\n")

mi_texto = "Esto es una prueba"
resultado = mi_texto.index("prueba") #De esta manera te indica el numero desde el cual comienza la palabra
print(resultado)

print("<----------->\n")

#Si quieres buscar una letra que se repite mas de una vez puedes agregar desde donde buscar ("a",5) de esta manera indicas que tiene que buscar desde el caracter 5 en adelante
mi_texto = "Esto es una prueba"
resultado = mi_texto.index("a",12) #De esta manera busca desde la posicion 12 en adelante
print(resultado)

print("<----------->\n")
#.rindex se encarga de buscar los caracteres de derecha a izquierda
mi_texto = "Esto es una prueba"
resultado = mi_texto.rindex("a",1,17) #De esta manera te indica el numero desde el cual comienza la palabra buscando de derecha a izquierda
print(resultado)

print("<----------->\n")



texto = input("Ingresa un texto: ")
letra = input("Ingresa una letra que este en el texto: ")
print(texto)
print(f"La letra que ingresaste se encuentra en la posicion: {texto.index(letra,9,21)}")

texto = input("Ingresa una cadena: ")
palabra = input("Ingresa una palabra: ")
print(f"La palabra {palabra} comienza desde el indice {texto.index(palabra)}")

#.rindex funciona para hacer busquedas de derecha a izquierda
texto = str(input("Ingresa una cadena: "))
palabra = input("Ingresa una letra: ")
print(f"La ultima aparicion de la letra {palabra} es {texto.rindex(palabra)}")


#texto = "La programación en Python es divertida"
#palabra =""""  "Hola" #input("Ingresa una palabra: ")
#if palabra in texto:
#    print(f"La palabra {palabra} se encuentra  desde la posicion "
#      f"{texto.index(palabra[0])} y termina en la posicion: {texto.rindex(palabra[-1])}")
#else:
#    print(f"La palabra {palabra} no se encuentra en el texto")""""
#La programación en Python es divertida

