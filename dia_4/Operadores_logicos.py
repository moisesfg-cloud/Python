"""
and y (True si dos declaraciones son True)
or o (True si al menos una declaración es True)
not no (invierte el valor del booleano)
"""
from dia_2.Conversiones_implicitas import texto

#Comparacion directa
mi_bool = 4 > 5 < 6
print(mi_bool)
print("<--------------------------->")

#Para que sea mas legible lo puedes poner entre parentesis
mi_bool = (4 < 5) and  (5== 2+3)
print(mi_bool)
print("<--------------------------->")

#Tambien se pueden buscar textos
mi_bool = "Este es un texto, breve"
busqueda = ('texto' in mi_bool) and ('breve' in mi_bool)
print(busqueda)
print("<--------------------------->")

mi_bool = "Este es un texto, breve"
busqueda = ('texto' not in mi_bool) and ('breve' in mi_bool)
print(busqueda)
print("<--------------------------->")

#Pregunta si a no es igual a 'a'
mi_bool = not ('a'=='a')
print(mi_bool)
print("<--------------------------->")

#Pregunta si no es igual o diferente a 'a', pero como en la comparacion si es igual a a nos dara como respuesta true osea verdadero
mi_bool = not ('a'!='a')
print(mi_bool)

print("<--------------------------->")

