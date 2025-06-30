import os
from pathlib import Path

#os sistema operativo
#path
ruta = os.getcwd() #obtener el directorio de trabajo actual
print(ruta)

ruta = os.makedirs('/Users/moisesferia/Desktop/otra') # Crear carpeta nueva


ruta = os.chdir('/Users/moisesferia/Desktop/otra') #cambiar directorio
cambio_ruta = os.getcwd()
print(cambio_ruta)


ruta = '/Users/moisesferia/Documents/Python/Python/dia_6/prueba.txt'
elemento = os.path.basename(ruta) #Nombre de base o nombre del archivo
print(elemento)

otra = '/Users/moisesferia/Documents/Python/Python/dia_6/prueba.txt'
elemento = os.path.dirname(otra) #Te brinda toda la ruta
elemento = os.path.split(otra) #Devuelve una tupla con ruta y archivo
print(elemento)


#Eliminar carpetas
os.rmdir('/Users/moisesferia/Desktop/otra/otro_archivo.txt.txt') #remover directorio

#Abrir arhivo en otra ruta
otro_archivo = open("/Users/moisesferia/Desktop/prueba.txt")
print(otro_archivo)


#Esto solo sirve para tener compatibilidad del archivo con difereten sistemas operativos
carpeta = Path('/Users/moisesferia/Desktop/otra') / "otro_archivo2.txt"
archivo = carpeta / 'otro_achivo3.txt' #De esta manera se concatena y se crean rutas
mi_archivo = open(archivo)
print(mi_archivo.read())
