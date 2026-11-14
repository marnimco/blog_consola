import json
from blog.modelos import Autor, Post

# Tupla
estados_post = ("borrador", "publicado", "archivado")

def cargar_posts():
    try:
        with open("posts.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        print("No se pudieron cargar los posts desde posts.json.")
        return []

    if not isinstance(datos, list):
        print("Error. Los datos deben ser una lista.")
        return []

    lista_posts = []

    for dato in datos:
        try:
            datos_autor = dato["autor"]

            autor = Autor(
                datos_autor["nombre"],
                datos_autor["bio"],
                datos_autor["especialidad"],
                datos_autor["redes_sociales"]
            )

            post = Post(
                dato["id"],
                dato["titulo"],
                autor,
                dato["categoria"],
                dato["contenido"],
                dato["tags"],
                dato["estado"]
            )

            if not isinstance(post.titulo, str) or not isinstance(post.tags, list):
                print("Error. Un post tiene datos incorrectos.")
                continue

            tags_validos = True
            for tag in post.tags:
                if not isinstance(tag, str):
                    tags_validos = False

            if not tags_validos:
                print("Error. Un post tiene tags incorrectos.")
                continue

            lista_posts.append(post)

        except (KeyError, TypeError):
            print("Error. Un post tiene datos incompletos o incorrectos.")

    return lista_posts


def guardar_posts(posts):
    lista_datos = []

    for post in posts:
        lista_datos.append(post.a_diccionario())

    try:
        with open("posts.json", "w", encoding="utf-8") as archivo:
            json.dump(lista_datos, archivo, ensure_ascii=False, indent=4)

        print("Los posts se guardaron correctamente.")

    except (OSError, TypeError, AttributeError):
        print("Error. No se pudieron guardar los posts.")
