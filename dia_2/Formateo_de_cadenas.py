#format/ print("Mi auto es {} y de matricula {}".format(color_auto,matricula))
#print(f"El monto es: {valor}")
#NOTA: no importa que tipo de dato sea, se puede incluir para que sea mostrado
from time import process_time_ns

x = 10
y = 5
print("Mis numeros son: " + str(x) + " y " + str(y)) #Este ejercicio es usando una conversion
print("Mis numeros son: {} y {}".format(x,y)) #Metodo .format()
print(f"Mis numeros son: {x} y {y}\n") #Cadena Literal

color = "rojo"
matricula = "pda-24-30"

print(f"El auto es {color} y su matricula es {matricula}") #Cadena literal
print("El auto es color {} y su matricula es {}".format(color,matricula)) #Funcion format

moto = "italika"
modelo = "205z"
print(f"Tengo una moto {moto} que es modelo {modelo}")#Cadena literal
print("Tengo una moto {} que es modelo {}".format(moto,modelo))
print("Tengo una moto" , moto , "que es modelo",modelo)
