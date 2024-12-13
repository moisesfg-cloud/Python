

def revision(numero):
     return numero in range(100,1000)
"""Lo que estamos presenciando es, poder analizar un numero
si es que cuenta con 3 cifras o no"""
resultado =  revision(10)
print(resultado)


def revision_3_cifras(numero):
    return numero in range(100,1000)

suma = 586 + 402
resultado = revision_3_cifras(suma)
print(resultado)