# Metodos de escritura
#r solo lectura
#w escirtura - write
#a todo lo que se escriba sera ingresado al final
#writelines metodo, se puede pasar una lista de strings

archivo = open('prueba.txt','w')
archivo.write('Soy el nuevo texto\n') #De esta manera escribimos en el arcivo, se debe de abrir en el modo adecuado
archivo.write('mundo')
archivo.writelines(['hola','mundo','soy','moi'])
#Con un loop
lista = ['hola','mundo','soy','moi']
for i in lista:
    archivo.writelines(i + '\n')


archivo.close()
