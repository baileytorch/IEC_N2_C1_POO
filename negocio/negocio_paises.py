from datos.repositorios.repo_pais import listado_paises, guardar_pais
from datos.modelos.pais import Pais
from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error

def lista_paises(tabla_paises: PrettyTable):
    try:
        tabla_paises.field_names = ['Id', 'País', 'Nacionalidad', 'ISO 2', 'ISO 3', 'Habilitado']
        paises = listado_paises()
        for pais in paises:
            tabla_paises.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3, ('Deshabilitado','Habilitado')[pais.habilitado]])
        return tabla_paises
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_objeto_pais(pais, nacionalidad, iso2, iso3):
    try:
        nuevo_pais = Pais()
        nuevo_pais.pais = pais
        nuevo_pais.nacionalidad = nacionalidad
        nuevo_pais.iso2 = iso2
        nuevo_pais.iso3 = iso3
        guardar_pais(nuevo_pais)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def actualizar_objeto_pais(nombre_pais, nacionalidad, iso2, iso3, habilitado, pais:Pais):
    try:
        if nombre_pais != '':
            pais.pais = nombre_pais
        if nacionalidad != '':
            pais.nacionalidad = nacionalidad
        if iso2 != '':
            pais.iso2 = iso2
        if iso3 != '':
            pais.iso3 = iso3
        if habilitado != True:
            pais.habilitado = habilitado
        guardar_pais(pais)
    except Exception as error:
        print(f'{mensaje_error}{error}')