#**kwargs = "key word args " palabras clave

def suma(num1,num2,*args,**kwargs):

    print(f'El primer valor es {num1}')
    print(f'El primer valor es {num2}')

    for i in args:
        print(f'arg = {args}')


    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [500,100,200,300]
kwargs = {"x":'uno',"y":'dos',"z":'tres'}

#Formas de interpretacion

suma(1,3,*args,**kwargs)
#suma(1,3,500,100,200,300, x=5, y=3, z=4)

#EJERCICIO 1
def cantidad_atributos(**kwargs):
        return len(kwargs)
print(cantidad_atributos(x=1))

#EJERCICIO 2
def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    return lista

print(lista_atributos(x=4,y=5))

#EJERCICIO 3
def describir_persona(nombre,**kwargs):
    print(f'Caracteristicas de: {nombre}')
    for clave,valor in kwargs.items():
        print (f'{clave}: {valor}')
describir_persona("Papoi",color_ojos="cafe",piel="morada", raza = "minion" )