import sys
from auxiliares import nombre_app,version_app
from auxiliares import menu_superior,sub_menu_biblioteca,sub_menu_libros,sub_menu_prestamos
from auxiliares import opcion_volver,opcion_invalida
from presentacion.presentacion_pais import modificar_pais

def menu_principal():
    print(f'{nombre_app} v{version_app}')
    print(f'{'=' * len(nombre_app)}=={'=' * len(version_app)}\n')

    while True:
        for clave,valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input(f'Ingrese su opción [0-{len(menu_superior)-1}]')

        match opcion_usuario:
            case '1':
                while True:
                    for clave,valor in sub_menu_biblioteca.items():
                        print(f'[{clave}] - {valor}')

                    opcion_biblioteca = input(f'Ingrese su opción [0-{len(sub_menu_biblioteca)-1}]')
                    match opcion_biblioteca:
                        case '1':
                            modificar_pais()
                        case '2':
                            pass
                        case '3':
                            pass
                        case '0':
                            print(opcion_volver)
                            break
                        case _:
                            print(opcion_invalida)
            case '2':
                while True:
                    for clave,valor in sub_menu_libros.items():
                        print(f'[{clave}] - {valor}')
                
                    opcion_libro = input(f'Ingrese su opción [0-{len(sub_menu_libros)-1}]')
                    match opcion_libro:
                            case '1':
                                pass
                            case '2':
                                pass
                            case '3':
                                pass
                            case '0':
                                print(opcion_volver)
                                break
                            case _:
                                print(opcion_invalida)

            case '3':
                while True:
                    for clave,valor in sub_menu_prestamos.items():
                        print(f'[{clave}] - {valor}')
                                
                    opcion_prestamo = input(f'Ingrese su opción [0-{len(sub_menu_prestamos)-1}]')
                    match opcion_prestamo:
                        case '1':
                            pass
                        case '2':
                            pass
                        case '3':
                            pass
                        case '0':
                            print(opcion_volver)
                            break
                        case _:
                            print(opcion_invalida)

            case '0':
                print('Saliendo...')
                sys.exit()

            case _:
                print(opcion_invalida)