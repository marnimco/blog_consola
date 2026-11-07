
def listar_posts(lista):
    for post in lista:
        print(post["titulo"])
        print(post["autor"]["nombre"])
        print(post["estado"])


def buscar_por_titulo(lista, termino):
    resultados = []
    for post in lista:
        if termino.lower() in post["titulo"].lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    resultados = []
    for post in lista:
        for tags in post["tags"]:
            if tag.lower() == tags.lower():
                resultados.append(post)
                break
    return resultados
