
from blog.datos import estados_post

def validar_post(post):
    # Comprobar que el post es un diccionario
    if not isinstance(post, dict):
        print("Error. El post no es un diccionario.")
        return False

    # Comprobar que exista la clave "autor"
    if "autor" not in post:
        return False

    # Comprobar que el título existe en post
    if "titulo" not in post:
        return False

    # Comprobar que el título no esté vacío
    if post["titulo"] == "":
        return False

    # Comprobar que el contenido existe en post
    if "contenido" not in post:
        return False

    # Comprobar que el contenido no esté vacío
    if post["contenido"] == "":
        return False

    # Comprobar que autor es un diccionario
    if not isinstance(post["autor"], dict):
        print("Error. El autor no es un diccionario.")
        return False

    # Comprobar que autor tiene nombre
    if "nombre" not in post["autor"]:
        return False
    if post["autor"]["nombre"] == "":
        return False

    # Comprobar que tags es una lista
    if "tags" not in post:
        return False
    if not isinstance(post["tags"], list):
        print("Error. Los tags no son una lista.")
        return False

    # Comprobar que id existe en post
    if "id" not in post:
        return False

    # Comprobar que estado es un valor en estados_post
    if "estado" not in post:
        return False
    if post["estado"] not in estados_post:
        return False

    return True
