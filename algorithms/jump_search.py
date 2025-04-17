import math                              # O(1)
def jump_search(arr, target):
    n = len(arr)                         # O(1) 
    if n == 0:                           # O(1) 
        return -1                        # O(1) 

    step = int(math.sqrt(n))             # O(1)
    prev = 0                             # O(1)

    # Bucle: se ejecuta en el peor caso O(√n) veces
    while prev < n and arr[min(step, n) - 1] < target:  
        prev = step                      # O(1) 
        step += int(math.sqrt(n))        # O(1)
        if prev >= n:                    # O(1)
            return -1                    # O(1)

    # Este bucle se ejecuta como máximo O(√n) veces (tamaño del bloque)
    for i in range(prev, min(step, n)):  # O(√n)
        if arr[i] == target:             # O(1) 
            return i                   # O(1)
    return -1                            # O(1) 
