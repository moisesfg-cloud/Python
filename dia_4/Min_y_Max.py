#Sirven para detectar el minimo y el maximo en una coleccion


menor = min(2,14,45,34,222)
mayor = max(2,14,45,34,222)
print(menor)
print(mayor)

lista =  [2,14,45,34,222]
print(f'El minimo es: {min(lista)} y el maximo es:{max(lista)} ')

print("<------------------------->")

nombre = 'moises' #En los strings siempre debemos de buscar con las letras en minusculas
print(min(nombre))
print(max(nombre))

print("<------------------------->")

nombres = ['moises','sergio','yair']
print(min(nombres))
print(max(nombres))

print("<------------------------->")

#Como obtener el valor o el indice con min y max de un diccionario
dic = {'c1':34,'c2':50,'c3':80}
print(min(dic.values())) #De esta manera estamos solicitando que imprima el menor de los valores
print(min(dic)) #De esta manera estamos solicitando que imprima el menor de los indices del diccionario

print("<------------------------->")

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(edad_minima)
print(ultimo_nombre)