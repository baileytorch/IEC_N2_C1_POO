from datos.repositorios.repo_pais import listado_paises, guardar_pais
from datos.modelos.pais import Pais
from prettytable import PrettyTable

def lista_paises():
    tabla_paises = PrettyTable()
    tabla_paises.field_names = ['Id', 'País', 'Nacionalidad', 'ISO 2', 'ISO 3', 'Habilitado']
    paises = listado_paises()
    for pais in paises:
        tabla_paises.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3, ('Deshabilitado','Habilitado')[pais.habilitado]])
    print(tabla_paises)

def crear_objeto_pais(pais, nacionalidad, iso2, iso3):
    nuevo_pais = Pais()
    nuevo_pais.pais = pais
    nuevo_pais.nacionalidad = nacionalidad
    nuevo_pais.iso2 = iso2
    nuevo_pais.iso3 = iso3
    guardar_pais(nuevo_pais)