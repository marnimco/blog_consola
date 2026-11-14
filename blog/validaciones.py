from blog.modelos import Autor, Post
from blog.datos import estados_post


def validar_post(post):
    # Comprobar que el post es un objeto Post
    if not isinstance(post, Post):
        print("Error. El post no es un objeto Post.")
        return False

    # Comprobar que el título no esté vacío
    if post.titulo == "":
        return False

    # Comprobar que el contenido no esté vacío
    if post.contenido == "":
        return False

    # Comprobar que autor es un objeto Autor
    if not isinstance(post.autor, Autor):
        print("Error. El autor no es un objeto Autor.")
        return False

    # Comprobar que autor tiene nombre
    if post.autor.nombre == "":
        return False

    # Comprobar que tags es una lista
    if not isinstance(post.tags, list):
        print("Error. Los tags no son una lista.")
        return False

    # Comprobar que estado es un valor en estados_post
    if post.estado not in estados_post:
        return False

    return True
