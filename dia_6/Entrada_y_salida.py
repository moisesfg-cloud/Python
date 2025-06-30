#metodo open(),nos permite abrir los archivos
#read()  lee el archivo
mi_archivo = open('prueba.txt') #De esta manera abrimos el archivo para la lectura
#print(mi_archivo.read()) # Así se muestra lo que hay dentro de ese archivo
print(mi_archivo.readline())
print(mi_archivo.readline().rstrip()) #Para no dejar saltos usas rstrip
print(mi_archivo.readline())

for l in mi_archivo:
    print("Aqui dice: " + l)

mi_archivo1 = open('prueba.txt')
print(mi_archivo1.readlines()) # nos hace una lista, solo usar en archivos pequeños


mi_archivo.close() #Siempre debemos de cerrar el archivo
