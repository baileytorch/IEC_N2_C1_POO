from presentacion.menu import menu_principal


def main() -> int:
    try:
        menu_principal()
    except (EOFError, KeyboardInterrupt):
        print('\nSaliendo...')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())