import json


class Autor:
    def __init__(self,nombre,bio):
        self.nombre=nombre
        self.bio=bio


class Post:
    def __init__(self,titulo,contenido,estado,autor,tags):
        self.titulo=titulo
        self.contenido=contenido
        self.estado="borrador"
        self.autor=autor
        self.tags=tags

    def mostrar_resumen(self, post):
            print(f"Titulo:{post.titulo} Autor:{post.autor.nombre}")

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "contenido": self.contenido,
            "estado": self.estado,
            "autor": self.autor,
            "tags": self.tags,
        }


class Blog: 
    def __init__(self, posts=None): 
     if posts is None: 
        self.posts = [] 

     else:
         self.posts = posts

    def crear_post(self,post):
        self.posts.append(post)

    def listar_posts(self):
        for post in self.posts:
            self.mostrar_resumen(post)

    def buscar_por_titulo(self,termino):
        termino_buscado= str(termino).lower().strip()
        for post in self.posts:
            if termino_buscado in post.titulo.lower():
                self.mostrar_resumen(post)

    def filtrar_por_tag(self,tag):
        resultados_tag=[]
        for post in self.posts:
            for etiqueta in post.tags:
                if etiqueta.lower()==tag.lower():
                    resultados_tag.append(post)
                    break
            return resultados_tag
        
    def crear_post(self,nuevo_post):
        self.posts.append(nuevo_post)
        print("¡Post creado y agregado al blog con éxito!")

    def guardar_posts_en_json(self, posts, nombre_archivo):
        publicaciones = []
        for post in posts:
            if isinstance(post, dict):
                publicaciones.append(post)
                continue

            publicaciones.append({
                "titulo": post.titulo,
                "contenido": post.contenido,
                "estado": post.estado,
                "autor": {
                    "nombre": post.autor.nombre,
                    "bio": post.autor.bio,
                },
                "tags": post.tags,
            })

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(publicaciones, archivo, ensure_ascii=False, indent=4)
