from negocio.negocio_paises import crear_objeto_pais
from datos.repositorios.repo_pais import obtener_pais_nombre
from datos.modelos.pais import Pais

def solicitar_datos_pais():
    pais = input('Ingrese el nombre del país: ')
    nacionalidad = input('Ingrese nacionalidad: ')
    iso2 = input('Ingrese ISO 2 del país: ')
    iso3 = input('Ingrese ISO 3 del país: ')
    return(pais, nacionalidad, iso2, iso3)

def agregar_pais():
    pais, nacionalidad, iso2, iso3=solicitar_datos_pais()
    crear_objeto_pais(pais, nacionalidad, iso2, iso3)

def modificar_pais():
    pais, nacionalidad, iso2, iso3=solicitar_datos_pais()
    pais_encontrado = obtener_pais_nombre(pais)
    if type(pais_encontrado) == Pais():
        print(f'{pais_encontrado.id_pais}{pais_encontrado.pais} {pais_encontrado.nacionalidad} {pais_encontrado.iso2} {pais_encontrado.iso3}')
    # crear_objeto_pais(pais, nacionalidad, iso2, iso3)
    else:
        print(pais_encontrado)