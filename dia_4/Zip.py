#Combinar dos o mas listas entre tuplas, para poder ver los zip es necesario castearlos a listas

nombre = ['moises','valeria','hugo']
edades = [65,29,42]
ciudad = ['lima','mexico','españa']

combinados = list(zip(nombre,edades,ciudad))
for nombre,edades,ciudad in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudad} ")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales,paises))
for capitales,paises in combinados:
    print(f"La capital de {paises} es {capitales}")


marca = ['apple','italika','nike','gucci']
producto = ['iphone','250z','air mag','ropaa']
combinados = list(zip(marca,producto))
for marca, producto in combinados:
    print(f"La marca es {marca} y el producto es {producto}")
