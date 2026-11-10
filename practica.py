#  def buscar_por_posicion(self, posicion):
#     if posicion < 0 or posicion >= self.cantidad:
#         print(f"  ⚠ Posición {posicion} fuera de rango")
#         return None
#     return self.datos[posicion]

# import bisect
# from pasajero import Pasajero


# class ListaPython:
#     """Implementación de lista para Pasajeros utilizando métodos nativos de Python."""

#     def __init__(self, capacidad=None):
#         # En Python las listas son dinámicas; se guarda capacidad solo como límite lógico opcional
#         self.datos = []
#         self.capacidad = capacidad

#     
#     # 1. MÉTODOS ORIGINALES (Equivalentes a los que ya tenías en tu código)
#    
#     def añadir(self, pasajero):
#         """Agrega al final usando append()."""
#         if self.capacidad is not None and len(self.datos) >= self.capacidad:
#             print("  ⚠ La lista está llena")
#             return False
#         self.datos.append(pasajero)
#         return True

#     def encolar(self, pasajero):
#         """Equivalente a encolar de la cola (alias de añadir)."""
#         return self.añadir(pasajero)

#     def desencolar(self):
#         """Retira y retorna el primer elemento (índice 0) usando pop(0)."""
#         if not self.datos:
#             print("  ⚠ La cola está vacía")
#             return None
#         return self.datos.pop(0)

#     def ver_frente(self):
#         """Consulta el primer elemento sin extraerlo."""
#         if not self.datos:
#             print("  ⚠ La cola está vacía")
#             return None
#         return self.datos[0]

#     def listar(self):
#         """Itera directamente con enumerate() nativo."""
#         if not self.datos:
#             print("  (colección vacía)")
#             return
#         for i, pasajero in enumerate(self.datos):
#             print(f"  [{i}] {pasajero}")

#     def buscar(self, numero):
#         """Búsqueda lineal usando next() y una expresión generadora."""
#         return next((p for p in self.datos if p.numero == numero), None)

#     def buscar_por_posicion(self, posicion):
#         """Acceso con validación o manejo de índices nativos."""
#         if 0 <= posicion < len(self.datos):
#             return self.datos[posicion]
#         print(f"  ⚠ Posición {posicion} fuera de rango")
#         return None

#     def modificar(self, numero, nuevo_destino, nuevo_asiento):
#         """Actualiza atributos si el elemento existe."""
#         pasajero = self.buscar(numero)
#         if pasajero:
#             pasajero.destino = nuevo_destino
#             pasajero.asiento = nuevo_asiento
#             return True
#         return False

#     def eliminar_por_numero(self, numero):
#         """Busca el pasajero y lo elimina directamente con remove()."""
#         pasajero = self.buscar(numero)
#         if pasajero:
#             self.datos.remove(pasajero)
#             return True
#         return False

#     def copiar(self):
#         """Copia superficial usando el método nativo copy() de listas."""
#         nueva = ListaPython(self.capacidad)
#         nueva.datos = self.datos.copy()
#         return nueva

#     def longitud(self):
#         """Retorna el conteo usando len()."""
#         return len(self.datos)

#     def esta_vacia(self):
#         """Evalúa si la lista está vacía con la sintaxis booleana de Python."""
#         return len(self.datos) == 0

#     
#     # 2. MÉTODOS AGREGADOS (Nuevas operaciones incorporadas)
#    

#     def insertar(self, posicion, pasajero):
#         """Inserta en un índice arbitrario usando insert()."""
#         if self.capacidad is not None and len(self.datos) >= self.capacidad:
#             print("  ⚠ La lista está llena")
#             return False
#         if 0 <= posicion <= len(self.datos):
#             self.datos.insert(posicion, pasajero)
#             return True
#         print(f"  ⚠ Posición {posicion} inválida")
#         return False

#     def eliminar_por_posicion(self, posicion):
#         """Elimina y extrae un elemento en un índice específico con pop()."""
#         if 0 <= posicion < len(self.datos):
#             return self.datos.pop(posicion)
#         print(f"  ⚠ Posición {posicion} fuera de rango")
#         return None

#     def eliminar_por_valor(self, numero):
#         """Alias funcional de eliminar_por_numero."""
#         return self.eliminar_por_numero(numero)

#     def ordenar_asc(self):
#         """Ordena de menor a mayor in-place usando sort() con clave lambda."""
#         self.datos.sort(key=lambda p: p.numero)

#     def ordenar_desc(self):
#         """Ordena de mayor a menor in-place con reverse=True."""
#         self.datos.sort(key=lambda p: p.numero, reverse=True)

#     def reversar(self):
#         """Invierte la lista in-place con reverse()."""
#         self.datos.reverse()

#     def buscar_binaria(self, numero):
#         """Búsqueda binaria O(log n) usando el módulo nativo bisect."""
#         # Extrae las claves numéricas con list comprehension
#         numeros = [p.numero for p in self.datos]
#         idx = bisect.bisect_left(numeros, numero)
#         if idx < len(self.datos) and self.datos[idx].numero == numero:
#             return self.datos[idx]
#         return None

# from pasajero import Pasajero


# class ListaPythonHibrida:
#     """Implementación que combina métodos nativos de Python con comprensiones."""

#     def __init__(self, capacidad=None):
#         self.datos = []
#         self.capacidad = capacidad

#     
#     # 1. MÉTODOS ORIGINALES (Basados en tu cola / lista manual previa)
#    

#     def añadir(self, pasajero):
#         """Agrega al final validando capacidad con len() y usando append()."""
#         if self.capacidad is not None and len(self.datos) >= self.capacidad:
#             print("  ⚠ La lista está llena")
#             return False
#         self.datos.append(pasajero)
#         return True

#     def encolar(self, pasajero):
#         """Alias para añadir."""
#         return self.añadir(pasajero)

#     def desencolar(self):
#         """Extrae el primer elemento en O(1) lógico con pop(0)."""
#         if not self.datos:
#             print("  ⚠ La cola está vacía")
#             return None
#         return self.datos.pop(0)

#     def ver_frente(self):
#         """Consulta el primer elemento."""
#         if not self.datos:
#             print("  ⚠ La cola está vacía")
#             return None
#         return self.datos[0]

#     def listar(self):
#         """Imprime directamente combinando enumerate() con comprensión."""
#         if not self.datos:
#             print("  (colección vacía)")
#             return
#         [print(f"  [{i}] {p}") for i, p in enumerate(self.datos)]

#     def buscar(self, numero):
#         """Filtra con list comprehension y obtiene el primer resultado."""
#         coincidencias = [p for p in self.datos if p.numero == numero]
#         return coincidencias[0] if coincidencias else None

#     def buscar_por_posicion(self, posicion):
#         """Acceso directo en O(1) validado con len()."""
#         if 0 <= posicion < len(self.datos):
#             return self.datos[posicion]
#         print(f"  ⚠ Posición {posicion} fuera de rango")
#         return None

#     def modificar(self, numero, nuevo_destino, nuevo_asiento):
#         """Busca el pasajero y modifica sus atributos por referencia."""
#         pasajero = self.buscar(numero)
#         if pasajero:
#             pasajero.destino = nuevo_destino
#             pasajero.asiento = nuevo_asiento
#             return True
#         return False

#     def eliminar_por_numero(self, numero):
#         """Ubica el índice mediante comprensión y elimina con pop()."""
#         indices = [i for i, p in enumerate(self.datos) if p.numero == numero]
#         if indices:
#             self.datos.pop(indices[0])
#             return True
#         return False

#     def copiar(self):
#         """Copia superficial instantánea con comprensión de lista."""
#         nueva = ListaPythonHibrida(self.capacidad)
#         nueva.datos = [p for p in self.datos]
#         return nueva

#     def longitud(self):
#         """Longitud instantánea O(1) con len()."""
#         return len(self.datos)

#     def esta_vacia(self):
#         """Verificación booleana nativa."""
#         return len(self.datos) == 0

#     
#     # 2. MÉTODOS AGREGADOS
#  

#     def insertar(self, posicion, pasajero):
#         """Inserta en el índice indicado con insert() nativo."""
#         if self.capacidad is not None and len(self.datos) >= self.capacidad:
#             print("  ⚠ La lista está llena")
#             return False
#         if 0 <= posicion <= len(self.datos):
#             self.datos.insert(posicion, pasajero)
#             return True
#         print(f"  ⚠ Posición {posicion} inválida")
#         return False

#     def eliminar_por_posicion(self, posicion):
#         """Elimina y retorna el elemento en el índice indicado con pop()."""
#         if 0 <= posicion < len(self.datos):
#             return self.datos.pop(posicion)
#         print(f"  ⚠ Posición {posicion} fuera de rango")
#         return None

#     def eliminar_por_valor(self, numero):
#         """Alias para eliminar_por_numero."""
#         return self.eliminar_por_numero(numero)

#     def ordenar_asc(self):
#         """Quicksort funcional recursivo construido con comprensiones de listas."""
#         def quicksort(lista):
#             if len(lista) <= 1:
#                 return lista
#             pivote = lista[0]
#             menores = [p for p in lista[1:] if p.numero <= pivote.numero]
#             mayores = [p for p in lista[1:] if p.numero > pivote.numero]
#             return quicksort(menores) + [pivote] + quicksort(mayores)

#         self.datos = quicksort(self.datos)

#     def ordenar_desc(self):
#         """Quicksort descendente con comprensiones de listas."""
#         def quicksort_desc(lista):
#             if len(lista) <= 1:
#                 return lista
#             pivote = lista[0]
#             mayores = [p for p in lista[1:] if p.numero >= pivote.numero]
#             menores = [p for p in lista[1:] if p.numero < pivote.numero]
#             return quicksort_desc(mayores) + [pivote] + quicksort_desc(menores)

#         self.datos = quicksort_desc(self.datos)

#     def reversar(self):
#         """Inversión in-place con reverse() nativo."""
#         self.datos.reverse()

#     def buscar_binaria(self, numero):
#         """
#         Búsqueda binaria O(log n) combinando comprensión para extraer números
#         con el módulo nativo bisect.
#         """
#         import bisect
#         claves = [p.numero for p in self.datos]
#         idx = bisect.bisect_left(claves, numero)
#         if idx < len(self.datos) and self.datos[idx].numero == numero:
#             return self.datos[idx]
#         return None