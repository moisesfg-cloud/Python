#Los diccionarios se conforman de pares, por ejemplo:
# Celular : Dispositivo Vehiculo: Carro -> Se escriben entre llaves y el concepto con el valor ejemplo:
#Se esciben como cadenas de texto separando el concepto del valor con dos puntos y una coma por conecpto y valor
mi_diccionario = {'contraseña fb':'valor1','contraseña google':'valor2'}
#Para poder obtener el valor del concepto es asi:
valor = mi_diccionario["contraseña fb"] #De esta manera solicitamos que nos brinden el valor o significado del concepto
print(valor)

cliente = {'Nombre':'Moises','Edad':'24 años','Peso':'80 kg','Color de ojos':'cafes','Facebook':'MoisesFG','Instagram': '_moises_fg','Gamertag':'Killernoob27'}
pregunta = input("""
- Edad
- Nombre
- Facebook
- Instagram
- Tiktok
- Gamertag
- Peso
- Color de ojos
Menciona que es lo que deseas saber de mi: """)
pregunta = pregunta.capitalize() #Este metodo me ayuda a que si el usuario escirbe con minusculas y el concepto comienza con mayusculas, en automatico haga la conversion a que todo lo que ingrese el usuario comience con mayuscula
respuesta = cliente[pregunta]
print(f"La información solicitada es {pregunta}: {respuesta}")


print("<------------------->\n")

#Aqui tenemos un diccionario que contiene una lista y otro diccionario dentro del mismo
cliente = {'Nombre':'Moises','Edad':'24 años','Comida favorita':['Pizza','Molletes','Cereal'],'Redes sociales':{'Facebook':'MoisesFG','Instagram':'_moises_fg'}}
#Para imprimir la lista que esta dentro del diccionario sera de la siguiente manera
print(cliente['Comida favorita'])
print(cliente['Comida favorita'][2]) #De esta manera solicitamos de manera especifica que nos brinden el idice 2 del concepto comida favorita

print("<------------------->\n")
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper()) #De esta manera nos posicionamos en el concepto 2 y solicitamos el valor del incide 1 el cual queremos que sea mayuscula

print("<------------------->\n")

#AGREGAR VALORES
#Aqui tenemos un alista con dos conceptos y dos valores
dic = {1:'a',2:'b'}
print(dic)
dic[3] = 'c' #Aqui estamos asignando dentro del diccionario el concepto 3 que sera igual al valor 'c'
print(dic)

print("<------------------->\n")
#Para poder cambiar el valor de un concpeto sera asi:
dic = {1:'a',2:'b'}
print(dic)
dic[2] = 'B' #Aqui estamos cambiando el valor
print(dic)

print("<------------------->\n")
print(".KEYS") #Nos va a traer todas las llaves o conceptos
dic = {1:'a',2:'b'}
print(dic.keys())

print("<------------------->\n")
print(".VALUES") #Nos va a traer los valores de los conceptos
dic = {1:'a',2:'b'}
print(dic.values())

print("<------------------->\n")
print(".ITEMS")#Imprime todos los valores
dic = {1:'a',2:'b'}
print(dic.items())