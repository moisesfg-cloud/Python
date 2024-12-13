"""Solo tienen dos valores TRUE or FALSE
==igual a
!=diferente a
>mayor que
<menor que
>=mayor o igual que
<=menor o igual que
and y (True si dos declaraciones son True)
or o (True si al menos una declaración es True)
not no (invierte el valor del booleano)
"""

#Se puede declara de estas formas
numero = 5 != 2+3
print(numero)

numero = bool(5>2)
print(numero)

lista = [1,2,3,4,5]
valor = 3 in lista
print(valor)