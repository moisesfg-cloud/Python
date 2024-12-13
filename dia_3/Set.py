"""Son inmutables
Admiten cualquier tipo de valor
No estan ordenandos en indice
Son elementos unicos y en caso de estar duplicados son descartados en automatico
Solo acepta un argunemto
set([1,2,3,4]) Esta es una manera de declararlo se pueden poner dentro de los parentesis (),[] ó {] para que se tome como un argumento
{1,2,3,4}
"""

#Formas de declarar los set
mi_set = ((1,2,3,4))
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,4}
print(type(mi_set))
print(mi_set)

print("<------------------->\n")
#Que no se puede hacer en los set
#mi_set = ((1,2,3,4))
#mi_set[0] = 3
#mi_set = ((1,2,[3,4],4)) No se pueden crear listas
#mi_set = ((1,2,{3,4},4)) No se pueden crear diccionarios

#Que se puede hacer en set
mi_set = ((1,2,3,4))
print(2 in mi_set)
print(mi_set)

print("<------------------->\n")
mi_set = ((1,2,3,(4,5,6,7),6)) #Crear una tupla dentro de un set
print(type(mi_set))
print(mi_set)

print("<------------------->\n")
print(".UNION")
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #Se van a unir ambas variables omitiendo numeros repetidos
print(s3)

print("<------------------->\n")
print(".ADD") #Para agregar un valor a un set
s1 = {1,2,3}
s1.add(4)
print(s1)

print("<------------------->\n")
print(".REMOVE") #Remueve valores
s1 = {1,2,3}
s1.remove(2)
print(s1)

print("<------------------->\n")
print(".DISCARD") #Descarta valores
s1 = {1,2,3}
s1.discard(2)
print(s1)

print("<------------------->\n")
print(".CLEAR") #Descarta valores
s1 = {1,2,3}
s1.clear() #Limpia todo nuestro set 
print(s1)