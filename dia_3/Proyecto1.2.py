texto = input("""Ingresa un texto: 
""".lower())
print("\nIngresa tres letras de tu elección")
letras = []
letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))
letra1 = letras[0:1:2]
letra2 = letras[1]
letra3 = letras[2]
conteo1 = texto.count(letra1)
conteo2 = texto.count(letra2)
conte3 = texto.count(letra3)
print(f"La letra {letra1} aparece {conteo1} veces")
print(f"La letra {letra2} aparece {conteo2} veces")
print(f"La letra {letra3} aparece {conte3} veces")
separador= texto.split()
largo = (len(separador))
print(f"El texto tiene {largo} palabras")
separador.reverse()
union = " ".join(separador)
print(union)
print(f"Si invertimos el texto quedaria asi: {separador}".split("_"))
print("python" in texto)
