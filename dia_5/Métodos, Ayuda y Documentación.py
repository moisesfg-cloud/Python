#Los metodos: son funciones de los objetos, permiten manipularlos, analizarlos, ejetuctar acciones
dic = {'clave1':100,'clave2':500}
a =dic.popitem() #

print(a)
print(dic)
#Orden LIFO last-in,first-out -> Primero en entrar, ultimo en salir y ultimo en entrar, primero en salir
print("<----------------->")

print(".LSTRIP()")
#Este metodo o funcion hace que se eliminen los elementos del lado izquierdo, dentro de comillas se ingresan los elementos a eliminar
texto =",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,"
texto_limpio = texto.lstrip(',:%_#')
print(texto_limpio)
texto =",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,".lstrip(",:%_#")
print(texto)
#print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

print("<----------------->")

print(".INSERT")
#Con insert como primer parametro se ingresa el indice en donde se quiere colocar y el string que se colocara
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

print("<----------------->")

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG",}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)