from datos.modelos.pais import Pais
from peewee import IntegrityError, OperationalError, PeeweeException

def listado_paises():
    paises = Pais.select()
    if paises:
        return paises

def guardar_pais(pais:Pais):
    try:
        pais_guardado = pais.save()
        if pais_guardado == 1:
            print(f'Pais guardado con éxito. Id pais: {pais.id_pais}')
    except IntegrityError as e:
        print(f"Error de clave única o foránea: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")