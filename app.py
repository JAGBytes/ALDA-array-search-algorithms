import sys
import matplotlib.pyplot as plt
from data import execution_time_gathering  # Asegúrate de tener tu módulo actualizado

def print_results(table):
    print("Size | Lineal (Time, Mem) | Binary (Time, Mem) | Jump (Time, Mem)")
    for row in table:
        size, lineal_time, binary_time, jump_time, lineal_mem, binary_mem, jump_mem = row
        print(f"{size:<7} | [{lineal_time:>5}, {lineal_mem:>5}] | [{binary_time:>5}, {binary_mem:>5}] | [{jump_time:>5}, {jump_mem:>5}]")

def print_results_bin_jump(table):
    print("Size | Binary (Time, Mem) | Jump (Time, Mem)")
    for row in table:
        size, binary_time, jump_time, binary_mem, jump_mem = row
        print(f"{size:<7} | [{binary_time:>5}, {binary_mem:>5}] | [{jump_time:>5}, {jump_mem:>5}]")

def plot_results_bin_jump(table):
    sizes = [row[0] for row in table]
    binary_time = [row[1] for row in table]
    jump_time = [row[2] for row in table]
    binary_mem = [row[3] for row in table]
    jump_mem = [row[4] for row in table]

    # Gráfico de tiempos
    plt.figure(figsize=(10,5))
    plt.plot(sizes, binary_time, 'r--', marker='s', label='Binary Search')
    plt.plot(sizes, jump_time, 'g-.', marker='^', label='Jump Search')
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (ms)")
    plt.title("COMPARACIÓN: Binaria vs Saltos (Tiempo)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

    # Gráfico de memoria
    plt.figure(figsize=(10,5))
    plt.plot(sizes, binary_mem, 'r--', marker='s', label='Binary Search')
    plt.plot(sizes, jump_mem, 'g-.', marker='^', label='Jump Search')
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Memoria (bytes)")
    plt.title("COMPARACIÓN: Binaria vs Saltos (Memoria)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def plot_results(table):
    sizes = [row[0] for row in table]
    lineal_time = [row[1] for row in table]
    binary_time = [row[2] for row in table]
    jump_time = [row[3] for row in table]
    lineal_mem = [row[4] for row in table]
    binary_mem = [row[5] for row in table]
    jump_mem = [row[6] for row in table]

    # Gráfico combinado de tiempos
    plt.figure(figsize=(12,6))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, lineal_time, 'b-', marker='o', label='Lineal')
    plt.plot(sizes, binary_time, 'r--', marker='s', label='Binaria')
    plt.plot(sizes, jump_time, 'g-.', marker='^', label='Saltos')
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo (ms)")
    plt.title("TIEMPO de Búsquedas")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Gráfico combinado de memoria
    plt.subplot(1, 2, 2)
    plt.plot(sizes, lineal_mem, 'b-', marker='o', label='Lineal')
    plt.plot(sizes, binary_mem, 'r--', marker='s', label='Binaria')
    plt.plot(sizes, jump_mem, 'g-.', marker='^', label='Saltos')
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Memoria (bytes)")
    plt.title("MEMORIA de Búsquedas")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Configuración para pruebas intensivas
    config = {
    "min_size": 10_000_000,
    "max_size": 30_000_000,  # Más tamaños
    "step": 4_000_000,       # 10M, 14M, 18M, 22M, 26M, 30M (6 tamaños)
    "samples": 5              # Menos muestras
    }
    
    # Ejecutar pruebas (usando tu función measure_performance actualizada)
    full_data = execution_time_gathering.measure_performance(**config)
    
    print("\nRESULTADOS COMPLETOS:")
    print_results(full_data)
    plot_results(full_data)
    
    # Extraer solo datos de binaria y saltos para comparación detallada
    bin_jump_data = [
        [row[0], row[2], row[3], row[5], row[6]] 
        for row in full_data
    ]
    
    print("\nCOMPARATIVA BINARIA vs SALTOS:")
    print_results_bin_jump(bin_jump_data)
    plot_results_bin_jump(bin_jump_data)