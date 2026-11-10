import os

# DICCIONARIO: cada color tiene su etiqueta y su código de consola
COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

# TUPLA: respuestas afirmativas aceptadas. Es fija, por eso no es lista.
RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")


def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")


def imprimir_color(texto, color):
    codigo = COLORES.get(color, COLORES["BLANCO"])   # .get evita el error si el color no existe
    print(f"{codigo}{texto}{COLORES['RESET']}")


def imprimir_titulo(texto):
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()


def imprimir_exito(mensaje):
    imprimir_color(f"✓ {mensaje}", "VERDE")


def imprimir_error(mensaje):
    imprimir_color(f"✗ {mensaje}", "ROJO")


def imprimir_info(mensaje):
    imprimir_color(f"ℹ {mensaje}", "CYAN")


def confirmar(pregunta):
    # Devuelve True si el usuario respondió algo de la tupla RESPUESTAS_SI
    respuesta = input(f"{pregunta} (si/no): ").strip().lower()
    return respuesta in RESPUESTAS_SI


def validar_cedula(cedula):
    cedula = cedula.strip()
    return len(cedula) == 10 and cedula.isdigit()

def pedir_opcion_menu(titulo, lineas_menu, opciones_validas):
    """Muestra la interfaz del menú y no sale del bucle hasta que

    el usuario ingresa una de las opciones permitidas.

    :param titulo: Texto del encabezado.
    :param lineas_menu: Lista o tupla con las líneas de texto ya formateadas.
    :param opciones_validas: Colección con las teclas aceptadas (ej. ('1', '2',
    '3', '0')).
    :return: La opción elegida en mayúsculas y limpia de espacios.
    """
    imprimir_titulo(titulo)

    # Dibuja las líneas que componen el cuerpo del menú
    for linea in lineas_menu:
        print(f"  {linea}")
    print()

    # Bucle de validación interactiva
    while True:
        entrada = (
            input(f"{COLORES['AMARILLO']}Opción: {COLORES['RESET']}")
            .strip()
            .upper()
        )
        if entrada in opciones_validas:
            return entrada

        imprimir_error(
            f"Opción inválida. Opciones permitidas: {', '.join(opciones_validas)}"
        )