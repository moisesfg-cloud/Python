import os
import readline
from idlelib.macosx import addOpenEventSupport
from pathlib import Path

nombre = input("Ingresa tu nombre: ")
# Ruta sobre la que se va a trabajar y compatibilidad con otro OS
# carpeta = Path('/Users/moisesferia/Documents/Python/Python/Recetas')
guia = Path(Path.home(), "Documents", "Python", "Python", "Recetas")  # Devuelve el archivo
# Se brinda información
print(f"Bienvenido {nombre}, esta es la ruta sobre la ruta que debes de trabajar '{guia}' ")
# Menu de opciones para el usuario
opciones = 0
while opciones != 6:
    opcion = input("""
Selecciona una opcion:
Opcion 1  -  Leer recetas
Opcion 2  -  Crear nueva receta
Opcion 3  -  Crear nueva categoria
Opcion 4  -  Eliminar receta
Opcion 5  -  Eliminar categoria
Opcion 6  -  Salir
""")
    match opcion:
        # Leer receta <-------------------------------------->
        case "1":
            categoria = input("""
- Carnes
- Ensaladas
- Pastas
- Postres
- Que categoria eliges:
                """).capitalize()
            if categoria is int:
                print("Caracter no valido")
                continue
            if categoria not in ['Carnes', 'Ensaladas', 'Pastas', 'Postres']:
                print("Recetario no encontrado")
                continue
            if categoria == "Carnes" or categoria == "Postres" or categoria == "Ensaladas" or categoria == "Pastas":
                guia2 = Path(Path.home(), "Documents", "Python", "Python", "Recetas", categoria)
                print(guia2)
                for i in Path(guia2).glob('*.txt'):
                    print(i.name)
                lectura = input("Que receta deseas leer:")
                if categoria is int:
                    print("Caracter no valido")
                guia3 = Path(Path.home(), "Documents", "Python", "Python", "Recetas", categoria, lectura)
                print(guia3.read_text())
            # Crear receta <-------------------------------------->
        case "2":
            categoria = input("""
- Carnes
- Ensaladas
- Pastas
- Postres
Que categoria eliges:
                """).capitalize()
            if categoria is int:
                print("Caracter no valido")
            if categoria not in ['Carnes', 'Ensaladas', 'Pastas', 'Postres']:
                print("Recetario no encontrado")
                continue
            guia2 = Path(Path.home(), "Documents", "Python", "Python", "Recetas", categoria)
            nombre_archivo = input("Ingresa el nombre de tu nueva receta: ")
            sufijo = nombre_archivo + ".txt"
            nuevo = guia2 / sufijo

            nuevo.write_text("Aquí puedes escribir tu receta")
            # Crear categoría <-------------------------------------->
        case "3":
            categoria_nueva = input("Ingresa el nombre de la nueva categoria: ").capitalize()
            if categoria_nueva is int:
                print("Caracter no valido")
            ruta = os.makedirs(f"/Users/moisesferia/Documents/Python/Python/Recetas/{categoria_nueva}")
            # Eliminar receta
        case "4":
            borrar_receta = input("""
- Carnes
- Ensaladas
- Pastas
- Postres
Que categoria eliges:
            """).capitalize()
            guia2 = Path(Path.home(), "Documents", "Python", "Python", "Recetas", borrar_receta)
            for i in Path(guia2).glob('*.txt'):
                print(i)
            eliminar = input("Ingresa el nombre de la receta que deseas eliminar: ").capitalize()
            guia3 = Path(Path.home(), "Documents", "Python", "Python", "Recetas", borrar_receta,eliminar)
            print(guia3)
            delete = os.remove(guia3)
            # Eliminar categoría
        case "5":
            eliminar_categoria = input("Ingresa el nombre de la categoria que deseas eliminar: ").capitalize()
            if eliminar_categoria is int:
                print("Caracter no valido")
            ruta_a_eliminar = os.rmdir(f'/Users/moisesferia/Documents/Python/Python/Recetas/{eliminar_categoria}')
            # Salir
        case "6":
            print("Saliendo del recetario")
            break
        case _:
            print("Opción no válida")