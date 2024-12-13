#La palabra clave es def, esta palabra le dice a python que todo lo que se va a escribir es una funcion,
#siempre con minusculas

def mi_funcion(nombre): #Se le puede agragar un avariable aunque no sepas cual sera el valor
    """
    Siempre hay que escribir una breve explicación
        sobre cual es la tarea de la funcion
        Para que se imprima lo que esta dentro del "print" de la
        funcion debes de llamar a la funcion de nuevo
    """
    print("Hola " + nombre)
mi_funcion("Moises") # Se asigna el valor de la variable que se ingreso al principio de la funcion


def funcion(saludar):
    print(saludar)
funcion("¡Hola mundo!")



def saludar():
    print("¡Hola mundo!")


nombre_persona = "Luis"
def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')


un_numero = 3

def cuadrado(un_numero):
    print(un_numero ** 2)
cuadrado(un_numero)

