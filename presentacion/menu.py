from collections.abc import Callable

from auxiliares import (
    menu_biblioteca,
    menu_libros,
    menu_prestamos,
    menu_superior,
    nombre_app,
    opcion_invalida,
    opcion_volver,
    version_app,
)
from auxiliares.opciones_menu import menu_reportes
from presentacion.presentacion_pais import mostrar_paises


def _ejecutar_menu(
    opciones: dict[str, str],
    acciones: dict[str, Callable[[], None]],
    mensaje_salida: str = opcion_volver,
) -> None:
    while True:
        for clave, valor in opciones.items():
            print(f'[{clave}] - {valor}')

        opcion = input('Ingrese su opción: ').strip()
        if opcion not in opciones:
            print(opcion_invalida)
        elif opcion == '0':
            print(mensaje_salida)
            return
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print('Esta opción aún no está implementada.\n')


def _menu_biblioteca() -> None:
    _ejecutar_menu(menu_biblioteca, {'1': mostrar_paises})


def _menu_libros() -> None:
    _ejecutar_menu(menu_libros, {})


def _menu_prestamos() -> None:
    _ejecutar_menu(menu_prestamos, {})


def _menu_reportes() -> None:
    _ejecutar_menu(menu_reportes, {})


def menu_principal() -> None:
    print(f'{nombre_app} v{version_app}')
    print('=' * (len(nombre_app) + len(version_app) + 2))

    _ejecutar_menu(
        menu_superior,
        {
            '1': _menu_biblioteca,
            '2': _menu_libros,
            '3': _menu_prestamos,
            '4': _menu_reportes,
        },
        'Saliendo...\n',
    )
