from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desencolar(self):
        if self.cantidad == 0:
            print("  ⚠ La cola está vacía")
            return None
        
        eliminado = self.datos[0]

        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return eliminado

    def ver_frente(self):
        if self.cantidad == 0:
            print("  ⚠ La cola está vacía")
            return None

        return self.datos[0]

    def buscar(self, numero):
        if self.cantidad == 0:
            print("  ⚠ La cola está vacía")
            return None

        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return self.datos[i]
                
        return None

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pasajero = self.buscar(numero)
        if pasajero:
            pasajero.destino = nuevo_destino
            pasajero.asiento = nuevo_asiento
            return True
        return False

    def eliminar_por_numero(self, numero):
        posicion = -1
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                posicion = i
                break

        if posicion == -1:
            return False

        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return True

    def copiar(self):
        nueva_cola = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])
        return nueva_cola
    
    def insertar(self, posicion, pasajero):
        """Inserta un pasajero en una posición específica desplazando a la derecha."""
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False

        if posicion < 0 or posicion > self.cantidad:
            print(f"  ⚠ Posición {posicion} inválida")
            return False

        # Desplazamiento hacia la derecha desde el último elemento hasta 'posicion'
        for i in range(self.cantidad, posicion, -1):
            self.datos[i] = self.datos[i - 1]

        self.datos[posicion] = pasajero
        self.cantidad += 1
        return True

    def buscar_binaria(self, numero):
        """Búsqueda binaria por número (asume que la lista está ordenada ascendentemente)."""
        inicio = 0
        fin = self.cantidad - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.datos[medio].numero == numero:
                return self.datos[medio]
            elif self.datos[medio].numero < numero:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None

    def eliminar_por_posicion(self, posicion):
        """Elimina el pasajero en la posición indicada y compacta hacia la izquierda."""
        if posicion < 0 or posicion >= self.cantidad:
            print(f"  ⚠ Posición {posicion} fuera de rango")
            return None

        eliminado = self.datos[posicion]

        # Desplazamiento hacia la izquierda para tapar el hueco
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return eliminado

    def ordenar_asc(self):
        """Ordenamiento Burbuja de menor a mayor según el atributo 'numero'."""
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    # Intercambio manual de posiciones
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):
        """Ordenamiento Burbuja de mayor a menor según el atributo 'numero'."""
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    # Intercambio manual de posiciones
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def reversar(self):
        """Invierte los elementos en el arreglo in-place usando dos punteros."""
        izquierda = 0
        derecha = self.cantidad - 1

        while izquierda < derecha:
            aux = self.datos[izquierda]
            self.datos[izquierda] = self.datos[derecha]
            self.datos[derecha] = aux
            izquierda += 1
            derecha -= 1

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0