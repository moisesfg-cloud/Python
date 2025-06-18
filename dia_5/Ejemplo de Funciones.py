precios_cafe = [('capuchino',2),('expresso',1.2),('moka',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0 #El precio comienza en 0
    cafe_mas_caro = '' #Comienza en string vacio

    for cafe,precio in lista_precios:
        if precio > precio_mayor: #Si el precio es mayor a precio mayor
            precio_mayor = precio #Que tenga el contenido en precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)
cafe,precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es {cafe} ya que su precio es de {precio}')
