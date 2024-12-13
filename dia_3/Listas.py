#Objetos, secuencia de elementos oredandos, strin, integer, float, diferentes datos al mismo tiempo entre [], se pueden tener listas dentro de listas
mi_lista = ["a","b","c"]
resultado = len(mi_lista) #De esta manera podemos obtener el largo de nuestra lista
indice = mi_lista.index("a") #De esta manera solo me dara el numero de posicion en el que se encuentra la letra o caracter
print(indice)
idice1 = mi_lista[0] #De esta manera solo me brindara la letra o carater que se encuentra en esa posicion
print(idice1)
print(type(mi_lista))

print("<------------------->\n")

otra_lista = ['hola',55,6.1]
largo = len(otra_lista)
print(largo)
indice = otra_lista.index(55) #Se usa para saber posicion del caracter que se ingreso en los parentesis
print(indice)
indice1 = otra_lista[2] #Se usa para saber que caracter usa la posicion que ingresas en las corchetes
print(indice1)

print("<------------------->\n")

#Este es un ejercicio para sobrescribir los valores dentro de las listas
lista = ['a','b','c'] #Creamos listas con valores
lista [0] = "alfa" #Ingresamos entre corchetes el numero de indice a sobreescirbir y atraves de signos de igual y comillas establecemos el nuevo valor
print(lista) #Imprimimos la salida del nuevo valor dentro de la lista

print("<------------------->\n")

print("CONCATENACIONES DE LISTAS")
mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
print(mi_lista +  mi_lista2) # Aquí se estan concatenando las listas

print("<------------------->\n")

print("APPEND") #agregar elemento a la lista original
mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "alfa" # De esta manera cambiamos el valor del indice 0 porque recuerda que las listas son mutables
mi_lista3.append("g") #Aqui estamos agregando un nuevo valor a la lista
print(mi_lista3)

print("<------------------->\n")

print("POP") #eliminar
mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista3.pop(2) #Para eliminar un valor se tiene que ingresar el numero de indice que ocupa el caracter
mi_lista3.pop() #Si lo dejas sin valor interpreta que quieres eliminar el ultimo valor
eliminado = mi_lista3.pop(2)#Para almacenar un valor anteriormente eliminado con pop debes de agregarle una variable
print(mi_lista3)
print(eliminado)


print("<------------------->\n")

print("SORT")#ORDENDAR
lista = ['b','g','o','a','d']
lista.sort() #Indicamos que se ordene la lista de manera alfabetica
print(lista)

print("<------------------->\n")


print("REVERSE")#pone lo ultimo primero
lista = ['b','g','o','a','d']
lista.reverse()
print(lista)