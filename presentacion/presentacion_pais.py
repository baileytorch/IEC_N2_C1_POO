from negocio.negocio_paises import crear_objeto_pais,actualizar_objeto_pais,lista_paises
from datos.repositorios.repo_pais import obtener_pais_nombre
from prettytable import PrettyTable
from auxiliares.info_app import mensaje_nombre_pais,mensaje_error

def mostrar_paises():
    tabla_paises = PrettyTable()
    try:        
        tabla_paises = lista_paises(tabla_paises)
        print(tabla_paises)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def solicitar_datos_pais():
    try:
        pais = input(mensaje_nombre_pais)
        nacionalidad = input('\nIngrese nacionalidad: ')
        iso2 = input('Ingrese ISO 2 del país: ')
        iso3 = input('Ingrese ISO 3 del país: ')
        return(pais, nacionalidad, iso2, iso3)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def agregar_pais():
    try:
        pais, nacionalidad, iso2, iso3=solicitar_datos_pais()
        crear_objeto_pais(pais, nacionalidad, iso2, iso3)
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