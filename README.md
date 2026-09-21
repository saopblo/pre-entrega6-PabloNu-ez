"Proyecto sistema blog"
El proyecto es un sistema de blog, donde el usuario va poder ejecutar distintas funciones, desde ver, buscar y filtrar posts. Con la nueva funcion de crear posts y guardar datos en json.

Estructuras de Archivos y Modulos-

La estructura del sistema esta compuesta por una serie de modulos y un archivo.py donde se orquestara el funcionamiento principal.
Encontraremos carpetas converitdas en paquetes por el uso del __init__.py y dentro de cada uno modulos que cumpliran una funcion.
 `main.py`: Punto de entrada que coordina el menu.
 `modelos.py`: Contiene las clases del dominio (`Autor`, `Post`, `Blog`).
 `datos.py`: Se encarga de cargar y guardar la información en disco.
 `posts.json`: Archivo de texto estructurado para conservar los datos.

Clases Principales y Responsabilidades-

Autor:Modela al creador del post (atributos como `nombre` y `bio`).
Post :Modela la publicación y relaciona la instancia de `Autor` mediante composición.
Blog: Centraliza la colección de posts y los métodos de búsqueda, filtrado, listado y creación

Persistencia de Datos (JSON)

Guardado (Serialización): Los objetos `Post` y `Autor` se convierten en diccionarios planos mediante el método `.to_dict()` antes de pasarse a `json.dump()`.
Carga (Rehidratación): Al arrancar el programa, los diccionarios leídos con `json.load()` se reconvierten en instancias de las clases `Post` y `Autor`

A diferencia de la entrega anterior, incluimos un pasaje de diccionarios planos a clases y objetos.
Los datos ya no se pierden al cerrar la terminal gracias al archivo `posts.json`

Se mantiene la ejecucion con el comando python main.py