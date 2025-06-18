#Combinar dos o mas listas y las combina encerrandolas entre tuplas, para poder ver los zip es necesario castearlos a listas

nombre = ['moises','valeria','hugo']
edades = [65,29,42]
ciudad = ['lima','mexico','españa']

combinados = list(zip(nombre,edades,ciudad))
for nombre,edades,ciudad in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudad} ")

print("<-------------------------->")

capital = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
pais = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(capital,pais))
for capitales,paises in combinados:
    print(f"La capital de {pais} es {capital}")

print("<-------------------------->")

marca = ['apple','italika','nike','gucci']
producto = ['iphone','250z','air mag','ropaa']
combinados = list(zip(marca,producto))
for marca, producto in combinados:
    print(f"La marca es {marca} y el producto es {producto}")
