"""Son inmutables
Se usan ya sea con 'un dia' comillas o con parentesis ('un dia')
Ocupan menos espacio de memoria
Las usaremos en Estructuras que no queremos que sean modificadas
"""
mi_tuple = (1,2,(10,20),3,4)
print(mi_tuple)

print("<----------->\n")

#Ahora solo para que nos devuelva el indice que esta en el segundo tuple se tiene que declarar asi:
print(mi_tuple[2][1]) #Nos posicionamos en el indice 2 que pertenece al segundo tuple y solicitamos el valor que esta en el indice 1

print("<----------->\n")
#Ahora vamos a asigar un valor de la tupla a una variable
mi_tuple = (1,2,3)
x,y,z = mi_tuple
print(x,y,z)
#Esto solo se puede hacer si se cuentan con la misma cantidad de valores y variables, tambien se puede hacer con listas y diccionarios
print("<----------->\n")

mi_tuple = (1,2,3,1,1,3,2)
print(len(mi_tuple)) #Saber el largo de la tupla

print("<----------->\n")

print(".COUNT") # Nos ayuda a saber cuantas veces se repite algun valor
mi_tuple = (1,2,3,2)
print(mi_tuple.count(1)) #Nos brindara cuantas veces se repite el numero 1
print(mi_tuple.index(2)) # Me indica en que numero del indice se encuentra

print("<----------->\n")
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_tupla = list(mi_tupla)
mi_lista= mi_tupla
print(mi_lista)