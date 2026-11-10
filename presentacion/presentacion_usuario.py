from negocio.negocio_usuarios import lista_usuarios,crear_objeto_usuario
from datos.repositorios.repo_pais import obtener_pais_nombre
from prettytable import PrettyTable
from auxiliares.info_app import mensaje_nombre_pais,mensaje_error
from auxiliares.validaciones import validar_rut,validar_genero

def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    try:        
        tabla_usuarios = lista_usuarios(tabla_usuarios)
        print(tabla_usuarios)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def solicitar_datos_usuario():
    try:
        rut = nombre = apellido = correo = pais = fecha_nacimiento = genero = password = ''
        
        print('Ingrese Datos de Usuario')
        print('========================')
        
        while rut == '':
            rut = input('\nRUT (12.345.678-9): ')
            rut, mensaje = validar_rut(rut)
            print(mensaje)
            
        while nombre == '':
            nombre = input('\nNombre: ')
            
        while apellido == '':
            apellido = input('\nApellido: ')
            
        while correo == '':
            correo = input('\nCorreo: ')
        
        while pais == '':
            pais = input('\nNacionalidad: ')
            
        while fecha_nacimiento == '':
            fecha_nacimiento = input('\nFecha Nacimiento:  ')
            
        while genero == '':
            print('Seleccione Género')
            print('[1] Masculino')
            print('[2] Femenino')
            print('[3] Otro')
            genero = input('\nGénero: ')
            genero, mensaje = validar_genero(genero)
            print(mensaje)
            
        while password == '':
            password = input('\nContraseña: ')
            
        return(rut, nombre, apellido, correo, pais, fecha_nacimiento, genero, password)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def agregar_usuario():
    try:
        rut, nombre, apellido, correo, pais, fecha_nacimiento, genero, password = solicitar_datos_usuario()
        crear_objeto_usuario(rut,nombre,apellido,correo,pais,fecha_nacimiento,genero,password)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_pais():
    try:
        nombre_pais = input(mensaje_nombre_pais)
        pais_encontrado = obtener_pais_nombre(nombre_pais)
        if pais_encontrado:
            print('\nPais encontrado:')
            print(f'ID País: {pais_encontrado.id_pais}\nNombre País: {pais_encontrado.pais}\nNacionalidad: {pais_encontrado.nacionalidad}\nISO 2: {pais_encontrado.iso2}\nISO 3: {pais_encontrado.iso3}')
            nombre_pais = input('Ingrese el nombre del país (o ENTER para conservar): ')
            nacionalidad = input('Ingrese nacionalidad (o ENTER para conservar): ')
            iso2 = input('Ingrese ISO 2 del país (o ENTER para conservar): ')
            iso3 = input('Ingrese ISO 3 del país (o ENTER para conservar): ')
            actualizar_objeto_pais(nombre_pais,nacionalidad,iso2,iso3,True,pais_encontrado)
        else:
            print(pais_encontrado)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def eliminar_pais():
    try:
        nombre_pais = input(mensaje_nombre_pais)
        pais_encontrado = obtener_pais_nombre(nombre_pais)
        if pais_encontrado:
            print('Pais encontrado:')
            print(f'ID País: {pais_encontrado.id_pais}\nNombre País: {pais_encontrado.pais}\nNacionalidad: {pais_encontrado.nacionalidad}\nISO 2: {pais_encontrado.iso2}\nISO 3: {pais_encontrado.iso3}')
            actualizar_objeto_pais('','','','',False,pais_encontrado)
        else:
            print(pais_encontrado)
    except Exception as error:
        print(f'{mensaje_error}{error}')