
class Autor:
    def __init__(self, nombre, bio, especialidad, redes_sociales):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }


class Post:
    def __init__(self, id, titulo, autor, categoria, contenido, tags, estado):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.contenido = contenido
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor.a_diccionario(),
            "categoria": self.categoria,
            "contenido": self.contenido,
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self, posts):
        self.posts = posts

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, termino):
        resultados = []
        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)
        return resultados

    def filtrar_por_tag(self, tag):
        resultados = []
        for post in self.posts:
            for tags in post.tags:
                if tag.lower() == tags.lower():
                    resultados.append(post)
                    break
        return resultados

    def agregar_post(self, post):
        self.posts.append(post)
