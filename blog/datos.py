# Lista de diccionarios
perfil_autor = [
    {
        "nombre": "Juan Pérez",
        "bio": "Técnico electrónico",
        "especialidad": "Reparación de equipos electrónicos",
        "redes_sociales": ["@juan_perez", "@juan_perez"]
    },
    {
        "nombre": "María López",
        "bio": "Ingeniera en robótica",
        "especialidad": "Robótica y automatización",
        "redes_sociales": ["@maria_lopez", "@maria_lopez"]
    }
]

# Tupla
estados_post = ("borrador", "publicado", "archivado")

# Set
etiquetas_blog = {"Apple", "Samsung", "IOS", "Android", "Reparación", "Robótica", "Impresión 3D"}

# Lista
posts = [
    {
        "id": 1,
        "titulo": "Cambio de pantalla",
        "autor": perfil_autor[0],
        "categoria": "Reparación",
        "contenido": "Cómo reparar una pantalla de celular",
        "tags": ["Pantalla", "Reparación"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Cambio de batería",
        "autor": perfil_autor[0],
        "categoria": "Reparación",
        "contenido": "Cómo cambiar una batería",
        "tags": ["Batería", "Apple"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Impresión 3D de piezas",
        "autor": perfil_autor[1],
        "categoria": "Robótica",
        "contenido": "Cómo imprimir una pieza 3D",
        "tags": ["Impresión 3D", "Robótica"],
        "estado": "archivado"
    },
     {
            "id": 4,
            "titulo": "",
            "autor": perfil_autor[1],
            "categoria": "Robótica",
            "contenido": "Tipos de filamentos para impresión 3D",
            "tags": ["Impresión 3D", "Robótica"],
            "estado": "publicado"
    }
]