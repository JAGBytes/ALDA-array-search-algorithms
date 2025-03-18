from data import execution_time_gathering
import matplotlib.pyplot as plt

def print_results(table):
    print("Size | Linear Search (Time, Mem) | Binary Search (Time, Mem) | Jump Search (Time, Mem)")
    for row in table:
        size, linear_time, binary_time, jump_time, linear_mem, binary_mem, jump_mem = row
        print(f"{size:<5} | [{linear_time}, {linear_mem}] | [{binary_time}, {binary_mem}] | [{jump_time}, {jump_mem}]")

def plot_results(table):
    sizes = [row[0] for row in table]
    linear_times = [row[1] for row in table]
    binary_times = [row[2] for row in table]
    jump_times = [row[3] for row in table]
    linear_mem = [row[4] for row in table]
    binary_mem = [row[5] for row in table]
    jump_mem = [row[6] for row in table]

    # Gráfico de tiempos de ejecución
    plt.figure(figsize=(10,5))
    plt.plot(sizes, linear_times, marker='o', linestyle='-', label='Linear Search', color='blue')
    plt.plot(sizes, binary_times, marker='s', linestyle='--', label='Binary Search', color='red')
    plt.plot(sizes, jump_times, marker='^', linestyle='-.', label='Jump Search', color='green')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (units)")
    plt.title("Execution Time of Search Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

    # Gráfico de tiempos de ejecución (solo dos)
    plt.figure(figsize=(10,5))
    plt.plot(sizes, binary_times, marker='s', linestyle='--', label='Binary Search', color='red')
    plt.plot(sizes, jump_times, marker='^', linestyle='-.', label='Jump Search', color='green')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (units)")
    plt.title("Execution Time of Search Algorithms")
    plt.legend()
    plt.grid()
    plt.show()


    # Gráfico de uso de memoria
    plt.figure(figsize=(10,5))
    plt.plot(sizes, linear_mem, marker='o', linestyle='-', label='Linear Search', color='blue')
    plt.plot(sizes, binary_mem, marker='s', linestyle='--', label='Binary Search', color='red')
    plt.plot(sizes, jump_mem, marker='^', linestyle='-.', label='Jump Search', color='green')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Memory Usage of Search Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 90000
    step = 2000
    samples_by_size = 30

    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print_results(table)
    plot_results(table)
