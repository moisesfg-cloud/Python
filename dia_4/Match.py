#Coincidencias de patrones estructurales

serie = "N-02"
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

print("<-------------------------->")

serie = "N-02"
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")
        pass
print("<-------------------------->")

cliente = {'nombre':'moises',
            'edad':24,
            'ocupacion': 'estudiante'}

escuela = {'titulo':'uvm',
            'grado':{'grupo':'A',
                    'zona':'insurgentes'}}
elementos = [cliente,escuela,'libro']

for i in elementos:
    match i:
        case {'nombre': nombre,
            'edad':edad,
            'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)

        case {'titulo': titulo,
                    'grado':{'grupo':grupo,
                    'zona':zona}}:
                print("Es un estudiante")
                print(titulo,grupo,zona)
        case _:
            print("No se que seas")
