# Mostrar menú en consola

def mostrar_menu():
    print("MENÚ DEL BLOG")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe ingresar una opción")
        return None

    return opcion

def pedir_titulo():
    return input("Buscar por título: ").strip().lower()

def pedir_tag():
    return input("Buscar por tag: ").strip().lower()

