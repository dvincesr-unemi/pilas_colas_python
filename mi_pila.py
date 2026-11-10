from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTACIÓN (tabla 3) · recorre SIEMPRE del tope al fondo -------

    def desapilar(self):
        """Retira y retorna el elemento en el TOPE (último que entró).
        En una pila no hay que desplazar elementos: solo se limpia el tope.
        """
        if self.cantidad == 0:
            print("  ⚠ La pila está vacía")
            return None

        # El tope siempre está en cantidad - 1
        eliminado = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return eliminado

    def ver_tope(self):
        """Retorna el elemento que está en la cima sin extraerlo."""
        if self.cantidad == 0:
            print("  ⚠ La pila está vacía")
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        """Busca secuencialmente desde el TOPE hacia el FONDO."""
        if self.cantidad == 0:
            return None

        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return self.datos[i]
        return None

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        """Modifica datos del pasajero buscándolo desde el tope."""
        pasajero = self.buscar(numero)
        if pasajero:
            pasajero.destino = nuevo_destino
            pasajero.asiento = nuevo_asiento
            return True
        return False

    def eliminar_por_numero(self, numero):
        """Busca desde el tope y elimina desplazando a la izquierda."""
        posicion = -1
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                posicion = i
                break

        if posicion == -1:
            return False

        # Desplaza hacia la izquierda para cubrir el hueco
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return True

    def copiar(self):
        """Crea una réplica exacta manteniendo el orden desde el fondo al tope."""
        nueva_pila = MiPila(self.capacidad)
        # Se apilan de 0 a cantidad-1 para preservar la base y la cima
        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])
        return nueva_pila

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0