from negocio.negocio_paises import crear_objeto_pais

def solicitar_datos_pais():
    pais = input('Ingrese el nombre del país: ')
    nacionalidad = input('Ingrese nacionalidad: ')
    iso2 = input('Ingrese ISO 2 del país: ')
    iso3 = input('Ingrese ISO 3 del país: ')
    crear_objeto_pais(pais, nacionalidad, iso2, iso3)