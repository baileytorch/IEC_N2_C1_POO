def validar_rut(rut):
    return rut, mensaje

def validar_genero(genero):
    if genero not in ['1','2','3']:
        mensaje = 'Género Inválido'
        genero = ''
    else:
        mensaje = 'Género Válido'
    return genero, mensaje