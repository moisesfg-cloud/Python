"""Se repite mientras se cumplan las reglas o condicion,
Se detiene cuando algun parametro se deje de cumplir
break
continue
pass"""

moneda = 5
while moneda > 0: #Mientras monedas sea mayor a 0
    print(f"Tengo {moneda} monedas" )
    moneda -=1 #Igual a las que tengo menos 1
    """Puede ser de estas dos formas
    moneda = moneda -1 En cada loop se perdera una moneda, con esta linea
    moneda -= 1
    """
else:
    print("No tengo mas dinero")
print("<--------------------------->")

respuesta = 'S'
while respuesta == 'S':
    respuesta = input("Quieres continuar? (S/N): ").upper()

else:
    print("Gracias por su atencion")


print("<--------------------------->")
print("PASS") #Nos ayuda a pasar, se encarga de guardar el lugar para poder continuar con las ejecuciones

"""respuesta = 'S'
while respuesta == 'S':
   pass"""

print("<--------------------------->")

print("BREAK") #Interrumpe y nos permite salir
nombre = input("Tu nombre: ")
for i  in nombre:
    if i == 's':
     break
    print(i)

print("<--------------------------->")

print("CONTINUE") #Permite continuar sin el valor que se buscaba, si busco la 's' dentro de "moises" se imprime moie porque las s son el elemnto que se buscaba
nombre = input("Tu nombre: ")
for i  in nombre:
    if i == 's':
     continue
    print(i)

print("<--------------------------->")

print("<--------------------------->")

print("<--------------------------->")
