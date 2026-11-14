from blog.modelos import Autor, Post, Blog
from blog.datos import cargar_posts, guardar_posts, estados_post
from blog.menu import mostrar_menu, pedir_titulo, pedir_tag, pedir_datos_post
from blog.operaciones import mostrar_posts
from blog.validaciones import validar_post


if __name__ == "__main__":
    posts = cargar_posts()
    blog = Blog(posts)

    programa_activo = True

    while programa_activo:
        opcion = mostrar_menu()

        # Opción 1: Ver todos los posts
        if opcion == 1:
            mostrar_posts(blog.listar_posts())

        # Opción 2: Buscar por título
        elif opcion == 2:
            busqueda = pedir_titulo()
            resultados = blog.buscar_por_titulo(busqueda)
            mostrar_posts(resultados)

        # Opción 3: Filtrar por tag
        elif opcion == 3:
            busqueda = pedir_tag()
            resultados = blog.filtrar_por_tag(busqueda)
            mostrar_posts(resultados)

        # Opción 4: Crear nuevo post
        elif opcion == 4:
            datos = pedir_datos_post()

            if datos is not None:
                if datos["estado"] not in estados_post:
                    print("Error. El estado no es válido.")
                else:
                    autor = Autor(
                        datos["autor"]["nombre"],
                        datos["autor"]["bio"],
                        datos["autor"]["especialidad"],
                        datos["autor"]["redes_sociales"]
                    )

                    nuevo_id = 1

                    for post in blog.posts:
                        if post.id >= nuevo_id:
                            nuevo_id = post.id + 1

                    nuevo_post = Post(
                        nuevo_id,
                        datos["titulo"],
                        autor,
                        datos["categoria"],
                        datos["contenido"],
                        datos["tags"],
                        datos["estado"]
                    )

                    if validar_post(nuevo_post):
                        blog.agregar_post(nuevo_post)
                        print("Post creado correctamente.")
                    else:
                        print("Error. El post no es válido.")

        # Opción 5: Validar posts
        elif opcion == 5:
            for post in blog.listar_posts():
                resultado = validar_post(post)

                if resultado == True:
                    print(f"El post {post.id} es válido.")
                else:
                    print(f"El post {post.id} no es válido.")

        # Opción 6: Guardar posts en JSON
        elif opcion == 6:
            guardar_posts(blog.listar_posts())

        # Opción 7: Salir
        elif opcion == 7:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        # Opción inválida
        else:
            print("Opción inválida. Intentá de nuevo.")
