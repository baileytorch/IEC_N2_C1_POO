from datos.modelos.pais import Pais

def listado_paises():
    try:
        paises = Pais.select().where(Pais.habilitado == 1)
        if paises:
            return paises
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def obtener_pais_nombre(nombre):
    try:
        pais = Pais.get(Pais.pais == nombre)
        if pais:
            return pais
    except Exception as e:
        return f"Ha ocurrido un error: {e}"

def guardar_pais(pais:Pais):
    try:
        pais_guardado = pais.save()
        if pais_guardado == 1:
            print(f'Pais guardado con éxito. Id pais: {pais.id_pais}')
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")