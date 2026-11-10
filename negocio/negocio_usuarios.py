from prettytable import PrettyTable

from datetime import datetime

from datos.repositorios.repo_usuario import listado_usuarios_habilitados,guardar_usuario
from datos.modelos.usuario import Usuario
from auxiliares.info_app import mensaje_error

def lista_usuarios(tabla_usuarios: PrettyTable):
    try:
        tabla_usuarios.field_names = ['Id', 'RUT', 'Nombre Completo', 'Correo', 'Nacionalidad', 'Fecha Nacimiento', 'Género', 'Habilitado']
        usuarios = listado_usuarios_habilitados()
        for usuario in usuarios:
            nombre_completo = f'{usuario.nombre} {usuario.apellido}'
            tabla_usuarios.add_row([usuario.id_usuario, usuario.rut, nombre_completo, usuario.correo, usuario.pais, usuario.fecha_nacimiento, usuario.genero, ('Deshabilitado','Habilitado')[usuario.habilitado]])
        
    except Exception as error:
        print(f'{mensaje_error}{error}')
    return tabla_usuarios

def crear_objeto_usuario(rut,nombre,apellido,correo,pais,fecha_nacimiento,genero,password):
    try:
        nuevo_usuario = Usuario()
        nuevo_usuario.rut = rut
        nuevo_usuario.nombre = nombre
        nuevo_usuario.apellido = apellido
        nuevo_usuario.correo = correo
        nuevo_usuario.pais = int(pais)
        nuevo_usuario.fecha_nacimiento = datetime.strptime(fecha_nacimiento,'%d/%m/%Y')
        nuevo_usuario.genero = int(genero)
        nuevo_usuario.fecha_incorporacion = datetime.now()
        nuevo_usuario.habilitado = True
        nuevo_usuario.password = password
        guardar_usuario(nuevo_usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def actualizar_objeto_pais(nombre_pais, nacionalidad, iso2, iso3, habilitado, usuario:Usuario):
    try:
        if nombre_pais != '':
            usuario.usuario = nombre_pais
        if nacionalidad != '':
            usuario.nacionalidad = nacionalidad
        if iso2 != '':
            usuario.iso2 = iso2
        if iso3 != '':
            usuario.iso3 = iso3
        if habilitado != True:
            usuario.habilitado = habilitado
        guardar_pais(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')