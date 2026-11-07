
from blog.datos import posts
from blog.menu import mostrar_menu, pedir_titulo, pedir_tag
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


if __name__ == "__main__":
    programa_activo = True

    while programa_activo:
        opcion = mostrar_menu()

        # Opción 1: Ver todos los posts
        if opcion == 1:
            listar_posts(posts)

        # Opción 2: Buscar por título
        elif opcion == 2:
            busqueda = pedir_titulo()
            resultados = buscar_por_titulo(posts, busqueda)
            listar_posts(resultados)

        # Opción 3: Filtrar por tag
        elif opcion == 3:
            busqueda = pedir_tag()
            resultados = filtrar_por_tag(posts, busqueda)
            listar_posts(resultados)

        # Opción 4: Validar posts
        elif opcion == 4:
            for post in posts:
                resultado = validar_post(post)
                if resultado == True:
                    print(f"El post {post['id']} es válido.")
                else:
                    print(f"El post {post['id']} no es válido.")

        # Opción 5: Salir
        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        # Opción inválida
        else:
            print("Opción inválida. Intentá de nuevo.")



