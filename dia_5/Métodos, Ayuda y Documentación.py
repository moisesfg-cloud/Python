#Los metodos: son funciones de los objetos, permiten manipularlos, analizarlos, ejetuctar acciones
from traceback import print_tb

dic = {'clave':100,'clave2':500}
a =dic.popitem()

print(a)
print(dic)

print(".LSTRIP()")
#Este metodo o funcion hace que se eliminen los elementos del lado izquierdo, dentro de comillas se ingresan los elementos a eliminar
texto =",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,"
texto_limpio = texto.lstrip(',:%_#')
print(texto_limpio)
texto =",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,".lstrip(",:%_#")
print(texto)
#print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))


print(".INSERT")
#Con insert como primer parametro se ingresa el indice en donde se quiere colocar y el string que se colocara
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)