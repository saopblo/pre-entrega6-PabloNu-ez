from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import buscar_por_titulo, filtrar_por_tag, listar_posts
from blog.validaciones import validar_post
from blog.modelos import Autor
from blog.modelos import Post
from blog.modelos import Blog

def main():

    mi_blog=Blog(posts)
    while True:
        opcion=mostrar_menu()


        if opcion == 1:
            listar_posts(posts)




        elif opcion == 2:
            busqueda = input("\nBuscar por título: ").strip().lower()
            resultados = buscar_por_titulo(posts, busqueda)




            if resultados:
                print("\nResultados encontrados:")
                for post in resultados:
                    print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")
            else:
                print("No se encontraron posts que coincidan con la búsqueda.")




        elif opcion == 3:
            busqueda_tag = input("\nFiltrar por tag: ").strip().lower()
            resultados_filtrados = filtrar_por_tag(posts, busqueda_tag)
            




            if resultados_filtrados:
                print(f"\nPosts con el tag '{busqueda_tag}':")
                for post in resultados_filtrados:
                    print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")
            else:
                print("No se encontaron los tags buscados")




        elif opcion == 4:
            print("\n--- Crear nuevo post ---")
            titulo=input("Ingrese el titulo del post:").strip()
            contenido=input("Ingrese el contenido del post:").strip()
            estado="borrador"
            tags=None
            autor_actual= Autor(nombre="Pablo Nuñez",bio="Desarrollador Python")
            nuevo_post=Post(titulo=titulo, contenido=contenido, estado=estado, autor=autor_actual, tags=tags)
            mi_blog.crear_post(nuevo_post)



        
        elif opcion == 5:
            print("\n--- Validando publicaciones ---")
            for i, post in enumerate(posts, start=1):
                try:
                    es_valido, mensaje = validar_post(post)
                    if es_valido:
                        print(f"Post {i}: {mensaje}")
                    else:
                        print(f"Post {i}: error - {mensaje}")
                except Exception as e:
                    print(f"Post {i}: error inesperado - {e}")


        elif opcion == 6:
            print("\n--- Guardando publicaciones en JSON ---")
            mi_blog.guardar_posts_en_json(mi_blog.posts, "posts.json")
            print("Publicaciones guardadas correctamente en posts.json")
            
            


        elif opcion == 7:
            print("\n--- Gracias por utilizar el programa---")
            break



        else:
            print("Opción inválida, intenta de nuevo")
            




if __name__ == "__main__":
    main()