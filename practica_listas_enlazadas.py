class Nodo:
    """Un vagón: guarda un dato y la flecha (referencia) al siguiente vagón."""
    def __init__(self, data):
        self.data = data          # la carga del vagón
        self.next = None          # el enganche: al nacer no apunta a nadie


class ListaEnlazada:
    def __init__(self):
        self.head = None          # la cabeza: el primer nodo (None = lista vacía)
        self.cantidad = 0         # cuántos nodos hay

    # 1. INSERTAR AL INICIO: el nuevo pasa a ser la cabeza — O(1)
    def insertar_inicio(self, data):
        nuevo = Nodo(data)
        nuevo.next = self.head            # paso 1: el nuevo apunta a la cabeza actual
        self.head = nuevo                 # paso 2: la cabeza ahora es el nuevo
        self.cantidad = self.cantidad + 1

    # 2. INSERTAR AL FINAL: camina hasta el último y lo engancha ahí — O(n)
    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:             # lista vacía: el nuevo es la cabeza
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:    # mientras NO sea el último...
                actual = actual.next          # ...avanzo un vagón
            actual.next = nuevo               # el último ahora apunta al nuevo
        self.cantidad = self.cantidad + 1

    # 3. INSERTAR EN POSICIÓN: se detiene en el ANTERIOR (pos-1) — O(n)
    def insertar_en(self, pos, data):
        if pos < 0 or pos > self.cantidad:
            print("Posición no válida")
            return
        if pos == 0:                      # en la posición 0 es insertar al inicio
            self.insertar_inicio(data)
            return
        actual = self.head
        for _ in range(pos - 1):          # pos-1 saltos: quedo en el ANTERIOR
            actual = actual.next
        nuevo = Nodo(data)
        nuevo.next = actual.next          # paso 1: el nuevo se engancha al que sigue
        actual.next = nuevo               # paso 2: el anterior se engancha al nuevo
        self.cantidad = self.cantidad + 1

    # 4. BUSCAR: revisa vagón por vagón. Retorna la posición o -1 — O(n)
    def buscar(self, data):
        actual = self.head
        pos = 0
        while actual is not None:
            if actual.data == data:
                return pos                # lo encontré
            actual = actual.next
            pos = pos + 1
        return -1                         # recorrí todo y no estaba

    # 5. OBTENER: el dato de una posición. No hay datos[i]: hay que caminar — O(n)
    def obtener(self, pos):
        if pos < 0 or pos >= self.cantidad:
            print("Posición no válida")
            return None
        actual = self.head
        for _ in range(pos):              # pos saltos desde la cabeza
            actual = actual.next
        return actual.data

    # 6. MODIFICAR: busca el NODO con el dato viejo y le cambia la carga — O(n)
    def modificar(self, viejo, nuevo_dato):
        actual = self.head
        while actual is not None:
            if actual.data == viejo:
                actual.data = nuevo_dato  # cambia la carga; las flechas no se tocan
                return
            actual = actual.next
        print(viejo, "no existe")

    # 7. ELIMINAR POR POSICIÓN: el anterior se salta al nodo. Retorna el dato — O(n)
    def eliminar_por_posicion(self, pos):
        if pos < 0 or pos >= self.cantidad:
            print("Posición no válida")
            return None
        if pos == 0:                      # caso especial: quitar la cabeza
            quitado = self.head
            self.head = self.head.next
        else:
            anterior = self.head
            for _ in range(pos - 1):      # pos-1 saltos: quedo en el ANTERIOR
                anterior = anterior.next
            quitado = anterior.next       # el vagón que voy a quitar
            anterior.next = quitado.next  # el anterior se lo salta
        self.cantidad = self.cantidad - 1
        return quitado.data

    # 8. ELIMINAR POR VALOR: busca el ANTERIOR al que tiene el dato — O(n)
    def eliminar_por_valor(self, data):
        if self.head is None:
            print("Lista vacía")
            return
        if self.head.data == data:        # caso especial: es la cabeza
            self.head = self.head.next
            self.cantidad = self.cantidad - 1
            return
        anterior = self.head
        while anterior.next is not None and anterior.next.data != data:
            anterior = anterior.next      # miro UN vagón adelante
        if anterior.next is None:         # llegué al último sin encontrarlo
            print(data, "no existe")
            return
        anterior.next = anterior.next.next    # me salto el nodo
        self.cantidad = self.cantidad - 1

    # 9. INVERTIR: gira cada flecha hacia atrás con 3 variables — O(n)
    def invertir(self):
        anterior = None
        actual = self.head
        while actual is not None:
            siguiente = actual.next       # 1. guardo el resto del tren
            actual.next = anterior        # 2. giro la flecha hacia atrás
            anterior = actual             # 3. anterior avanza
            actual = siguiente            # 4. actual avanza
        self.head = anterior              # el último que vi es la nueva cabeza

    # 10. LONGITUD: cuántos nodos hay
    def longitud(self):
        return self.cantidad

    # Para ver la lista en pantalla (recorrido completo)
    def listar(self):
        actual = self.head
        while actual is not None:
            print(actual.data, end=" → ")
            actual = actual.next
        print("None")

    # Para comprobar resultados: convierte a una list de Python
    def a_lista(self):
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def __str__(self):
        return " → ".join(str(data) for data in self.a_lista()) + " → None"

    def __repr__(self):
        return f"ListaEnlazada({repr(self.a_lista())})"