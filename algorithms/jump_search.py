import math                              # O(1): Importación, se realiza una sola vez

def jump_search(arr, target):
    n = len(arr)                         # O(1): Obtener la longitud del array
    if n == 0:                           # O(1): Comprobación si el array está vacío
        return -1                        # O(1): Retorno inmediato si no hay elementos

    step = int(math.sqrt(n))             # O(1): Cálculo del tamaño del salto (sqrt(n) es O(1))
    prev = 0                             # O(1): Inicialización de 'prev'

    # Bucle: se ejecuta en el peor caso O(√n) veces
    while prev < n and arr[min(step, n) - 1] < target:  # Cada iteración: O(1)
        prev = step                      # O(1): Asignación de valor
        step += int(math.sqrt(n))        # O(1): Cálculo y actualización del salto
        if prev >= n:                    # O(1): Verificación si se ha superado el array
            return -1                    # O(1): Retorno en caso de no encontrar el target

    # Búsqueda lineal dentro del bloque identificado
    # Este bucle se ejecuta como máximo O(√n) veces (tamaño del bloque)
    for i in range(prev, min(step, n)):  # O(√n): Recorrido del bloque
        if arr[i] == target:             # O(1): Comparación en cada iteración
            return i                   # O(1): Retorno inmediato si se encuentra el target
    return -1                            # O(1): Retorno si no se encontró el target en el bloque
