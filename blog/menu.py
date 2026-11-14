def mostrar_menu():
    print("MENÚ DEL BLOG")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

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


def pedir_datos_post():
    print("CREAR NUEVO POST")

    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()
    nombre = input("Nombre del autor: ").strip()
    bio = input("Biografía del autor: ").strip()
    especialidad = input("Especialidad del autor: ").strip()
    red_social = input("Red social del autor: ").strip()
    categoria = input("Categoría: ").strip()
    tag = input("Tag: ").strip()
    estado = input("Estado (borrador/publicado/archivado): ").strip().lower()

    if titulo == "" or contenido == "" or nombre == "" or tag == "" or estado == "":
        print("Error. Los campos principales no pueden estar vacíos.")
        return None

    redes_sociales = []
    if red_social != "":
        redes_sociales.append(red_social)

    datos_autor = {
        "nombre": nombre,
        "bio": bio,
        "especialidad": especialidad,
        "redes_sociales": redes_sociales
    }

    datos_post = {
        "titulo": titulo,
        "contenido": contenido,
        "autor": datos_autor,
        "categoria": categoria,
        "tags": [tag],
        "estado": estado
    }

    return datos_post

