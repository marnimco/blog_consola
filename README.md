# Blog por consola

## Descripción

Este proyecto consiste en un blog desarrollado en Python que permite administrar publicaciones mediante un menú interactivo en la consola.

El programa utiliza Programación Orientada a Objetos (POO) y permite guardar y recuperar publicaciones mediante un archivo JSON.

## Funcionalidades

1. Ver todos los posts.
2. Buscar posts por título.
3. Filtrar posts por tag.
4. Crear un nuevo post.
5. Validar la estructura de los posts.
6. Guardar posts en JSON.
7. Salir del programa.

## Estructura del proyecto

- `main.py`: coordina la ejecución del programa.
- `blog/__init__.py`: identifica el paquete blog.
- `blog/datos.py`: contiene las funciones para cargar y guardar publicaciones.
- `blog/menu.py`: muestra el menú y recibe los datos ingresados por el usuario.
- `blog/modelos.py`: contiene las clases Autor, Post y Blog.
- `blog/operaciones.py`: muestra las publicaciones en la consola.
- `blog/validaciones.py`: contiene la función para validar los posts.
- `posts.json`: almacena las publicaciones.
- `.gitignore`: indica qué archivos y carpetas debe ignorar Git.

## Programación Orientada a Objetos

El programa utiliza tres clases principales:

- **Autor:** representa a una persona autora y contiene su información.
- **Post:** representa una publicación y contiene un objeto Autor.
- **Blog:** administra la lista de publicaciones y permite listarlas, buscarlas, filtrarlas y agregar nuevas.

## Persistencia JSON

Al iniciar el programa, se cargan las publicaciones desde `posts.json`.

Los datos almacenados como diccionarios se convierten en objetos de las clases Autor y Post.

Al seleccionar la opción de guardar, los objetos se convierten nuevamente en diccionarios y se almacenan en `posts.json`.

Esto permite conservar las publicaciones entre distintas ejecuciones del programa.

## Ejecución

Para ejecutar el programa, abrir una terminal en la carpeta principal del proyecto y escribir:

`python main.py`

El programa mostrará un menú interactivo para seleccionar sus funcionalidades.

Para conservar las publicaciones nuevas, seleccionar la opción 6 antes de salir.
