import time
import tracemalloc
from data import constants, data_generator
from algorithms.binary_search import binary_search
from algorithms.jump_search import jump_search
from algorithms.linear_search import linear_search

def measure_performance(min_size, max_size, step, samples):
    """Mide tiempo y memoria para los 3 algoritmos (lineal, binaria, saltos)."""
    results = []
    for size in range(min_size, max_size + 1, step):
        print(f"Procesando tamaño: {size}")
        
        # Generar datos y targets
        sorted_samples = [data_generator.get_sorted_random_list(size) for _ in range(samples)]
        unsorted_samples = [data_generator.get_random_list(size) for _ in range(samples)]
        targets = [data_generator.get_random_x(size) for _ in range(samples)]
        
        # Medir algoritmos
        linear_time, linear_mem = measure_algorithm(unsorted_samples, targets, linear_search)
        binary_time, binary_mem = measure_algorithm(sorted_samples, targets, binary_search)
        jump_time, jump_mem = measure_algorithm(sorted_samples, targets, jump_search)
        
        results.append([
            size,
            linear_time, linear_mem,
            binary_time, binary_mem,
            jump_time, jump_mem
        ])
    return results

def measure_algorithm(samples, targets, algorithm):
    """Mide tiempo (ms) y memoria (bytes) de un algoritmo."""
    times = []
    mem_usages = []
    
    for arr, target in zip(samples, targets):
        # Medición de memoria
        tracemalloc.start()
        # Medición de tiempo
        start_time = time.perf_counter()
        # Ejecutar algoritmo
        algorithm(arr, target)
        end_time = time.perf_counter()
        # Obtener memoria pico
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Calcular métricas
        elapsed_time = (end_time - start_time) * constants.TIME_MULTIPLIER  # ej: a milisegundos
        times.append(elapsed_time)
        mem_usages.append(peak)
    
    # Retornar mediana
    def _median(lst):
        sorted_lst = sorted(lst)
        n = len(sorted_lst)
        return sorted_lst[n // 2]
    
    return _median(times), _median(mem_usages)

if __name__ == "__main__":
    # Configuración para ver diferencias en TIEMPO (no memoria)
    results = measure_performance(
        min_size=10_000, 
        max_size=50_000, 
        step=10_000, 
        samples=10
    )
    
"""     # Encabezado legible
    print("\nTamaño | Lineal (ms) | Binaria (ms) | Saltos (ms) | Mem Lineal (B) | Mem Binaria (B) | Mem Saltos (B)")
    print("-" * 80)
    for row in results:
        size, t_lin, m_lin, t_bin, m_bin, t_jump, m_jump = row
        print(
            f"{size:6} | {t_lin:10.4f} | {t_bin:11.4f} | {t_jump:10.4f} | {m_lin:12} | {m_bin:13} | {m_jump:12}"
        ) """