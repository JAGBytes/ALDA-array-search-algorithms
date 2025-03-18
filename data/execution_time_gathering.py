import time
import tracemalloc
import random
import gc

from data import constants, data_generator
from algorithms.binary_search import binary_search
from algorithms.jump_search import jump_search
from algorithms.linear_search import linear_search

def take_time_and_memory_for_search_algorithm(samples_array, search_function):
    times = []
    mem_usages = []

    for arr, target in samples_array:
        # Forzar recolección de basura para minimizar interferencias
        gc.collect()

        # Iniciar trazado de memoria
        tracemalloc.start()
        start_snapshot = tracemalloc.take_snapshot()

        # Iniciar medición de tiempo con mayor precisión
        start_time = time.perf_counter()

        # Ejecutamos el algoritmo de búsqueda
        search_function(arr, target)

        end_time = time.perf_counter()

        # Tomamos una instantánea final de memoria y detenemos tracemalloc
        end_snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()

        # Cálculo de uso de memoria a partir de la comparación de instantáneas
        stats = end_snapshot.compare_to(start_snapshot, 'filename')
        # Calculamos el máximo uso (puedes probar también sum o average)
        peak_usage = max(stat.size_diff for stat in stats)

        # Multiplicamos el tiempo por la constante definida en constants.py
        elapsed_time = (end_time - start_time)
        exec_time = max(1, int(constants.TIME_MULTIPLIER * elapsed_time))

        times.append(exec_time)
        mem_usages.append(peak_usage)

    # Ordenamos para obtener la mediana (reduce el impacto de valores atípicos)
    times.sort()
    mem_usages.sort()
    median_time = times[len(times) // 2]
    median_mem = mem_usages[len(mem_usages) // 2]

    return median_time, median_mem

def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        # Generamos un array aleatorio y lo ORDENAMOS (necesario para binary y jump search)
        arr = sorted(data_generator.get_random_list(size))
        # Seleccionamos un target que sí esté en el array
        target = random.choice(arr)
        samples.append((arr, target))

    linear_res = take_time_and_memory_for_search_algorithm(samples, linear_search)
    binary_res = take_time_and_memory_for_search_algorithm(samples, binary_search)
    jump_res = take_time_and_memory_for_search_algorithm(samples, jump_search)

    return [linear_res, binary_res, jump_res]

def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print(f"\nProcesando tamaño: {size}")
        (linear_time, linear_mem), (binary_time, binary_mem), (jump_time, jump_mem) = take_times(size, samples_by_size)
        return_table.append([size, linear_time, binary_time, jump_time,
                             linear_mem, binary_mem, jump_mem])
    return return_table

if __name__ == "__main__":
    # Ajusta estos valores para ver más diferencia en memoria:
    # - Tamaños de 10,000 hasta 50,000 en incrementos de 10,000
    # - 5 muestras por tamaño
    results = take_execution_time(10_000, 50_000, 10_000, 5)

    print("\nTamaño | Linear Time | Binary Time | Jump Time | Linear Mem | Binary Mem | Jump Mem")
    for row in results:
        print(row)
