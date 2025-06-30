from pathlib import Path,PureWindowsPath # Ruta de windows pura
#PureWindowsPath Ruta de windows pura
#.read_text() lee archivos con pathlib
#Con el pathlib no es necesario abrir ni cerrar las carpetas

carpeta = Path('/Users/moisesferia/Documents/Python/Python/dia_6/prueba.txt')
print(carpeta.read_text()) #Lee el archivo asi con pathlib
print(carpeta.name) # Nos regresda el nombre del archivo
print(carpeta.suffix) #Funcion que nos brinda el sufijo del archivo
print(carpeta.stem) #Nos brinda el nombre sin la terminación

if not carpeta.exists(): #Nos brinda si existe o no
    print("Este archivo no existe")
else:
    print("Genial, existe")



ruta_windows = PureWindowsPath(carpeta) #Convierte la ruta a sistema operativo windows
print(ruta_windows)

