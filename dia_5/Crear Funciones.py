#La palabra clave es def, esta palabra le dice a python que todo lo que se va a escribir es una funcion,
#siempre con minusculas
print("<---------------------------------->")
 
def saludar_persona(nombre): #Declaracion de la función, y valor a recibir
    """
    Esta funcion sirve para saludar a las personas
    """
    print('Hola ' + nombre)
saludar_persona('Moises')
saludar_persona('Erik')
saludar_persona('juan')
print("<---------------------------------->")

def mi_funcion(nombre): #Se le puede agragar una variable aunque no sepas c®ual sera el valor
    """
    Siempre hay que escribir una breve explicación
        sobre cual es la tarea de la funcion
        Para que se imprima lo que esta dentro del "print" de la
        funcion debes de llamar a la funcion de nuevo
    """
    print("Hola " + nombre)
mi_funcion("Moises") # Se asigna el valor de la variable que se ingreso al principio de la funcion

print("<---------------------------------->")

def funcion(saludar):
    print(saludar)
funcion("¡Hola mundo!")

print("<---------------------------------->")

def saludar():
    print("¡Hola mundo!")
nombre_persona = "Luis"

print("<---------------------------------->")

def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')


print("<---------------------------------->")
un_numero = 3
def cuadrado(un_numero):
    print(un_numero ** 2)
cuadrado(un_numero)

print("<---------------------------------->")


nombre_persona = "Moidev"  #Crear una variable
def bienvenida (nombre_persona): #Tomar como argumento el nombre de una persona
    print(f"¡Binevenido {nombre_persona}!")
# bienvenida() - a esto se llama invoación


un_numero = 3
def cuadrado(un_numero):
    print(un_numero ** 2)
cuadrado(un_numero)
