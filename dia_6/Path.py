from pathlib import  Path
#crear o mover archivo
#enumerar archivos
#crear rutas basadas en string
#Crea rutas de acceso
#Acepta cadenas, como objetos
#Cuando deseas recuperar una porcion realtive_to

base = Path.home() #Devuelve una ruta al directorio actual, directorio principal
guia = Path(base,'Barcelona','Real madrid.txt')
print(base)
print(guia)

base1 = Path.home()
guia1 = Path(base1, 'Europa', 'españa', Path('Barcelona','Real madrid.txt'))
guia2 = guia1.with_name("La_Pedrera.txt")
print(guia1)
print(guia2)
print(guia1.parent) # Devuelve el antesesor, se pueden poner tantos paren como permita la ruta

#Numerar archivos
guia = Path(Path.home(),"Documents","Python","Python","dia_6")#Devuelve el archivo
for i in Path(guia).glob("**/*.txt"): #Incluye todas las subcarpetas o "*.txt" solo para una carptea
    print(i)

"""guia3 = Path("Europa","España")
en_europa = guia3.relative_to("Europa")
en_espania = guia3.relative_to("Europa","España")
print(en_europa)
print(en_espania)"""