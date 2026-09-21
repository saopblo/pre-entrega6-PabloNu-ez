# blog/validaciones.py

def validar_post(post):
   
    errores = []

    titulo = getattr(post, 'titulo', None) if not isinstance(post, dict) else post.get('titulo')
    contenido = getattr(post, 'contenido', None) if not isinstance(post, dict) else post.get('contenido')
    estado = getattr(post, 'estado', None) if not isinstance(post, dict) else post.get('estado')

   
    if not titulo or str(titulo).strip() == "":
        errores.append("El título no puede estar vacío.")

   
    if not contenido or str(contenido).strip() == "":
        errores.append("El contenido no puede estar vacío.")

  
    estados_permitidos = ("borrador", "publicado", "archivado")
    if estado not in estados_permitidos:
        errores.append(f"El estado '{estado}' no es válido (Debe ser borrador, publicado o archivado).")

    if errores:
        return False, " ".join(errores)

    return True, "El post es válido."