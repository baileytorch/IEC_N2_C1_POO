from datos.modelos.usuario import Usuario

def listado_usuarios_habilitados():
    try:
        usuarios = Usuario.select().where(Usuario.habilitado == True)
        if usuarios:
            return usuarios
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def listado_usuarios_deshabilitados():
    try:
        usuarios = Usuario.select().where(Usuario.habilitado == False)
        if usuarios:
            return usuarios
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def listado_usuarios():
    try:
        usuarios = Usuario.select()
        if usuarios:
            return usuarios
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def obtener_usuario_rut(rut):
    try:
        usuario = Usuario.get(Usuario.rut == rut)
        if usuario:
            return usuario
    except Exception as e:
        return f"Ha ocurrido un error: {e}"

def guardar_usuario(usuario:Usuario):
    try:
        pais_guardado = usuario.save()
        if pais_guardado == 1:
            print(f'Usuario guardado con éxito. Id: {usuario.id_usuario}')
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")