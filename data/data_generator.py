import random
from data import constants


from data import constants
import random

# Para búsqueda lineal (listas aleatorias no ordenadas)
def get_random_list(size, limit=constants.MAX_VALUE):
    return [random.randint(0, limit) for _ in range(size)]

# Para búsqueda binaria/saltos (listas ordenadas)
def get_sorted_random_list(size, limit=constants.MAX_VALUE):
    random_list = [random.randint(0, limit) for _ in range(size)]
    random_list.sort()
    return random_list

# Para pruebas deterministas (listas secuenciales)
def get_sequential_sorted_list(size):
    return list(range(1, size + 1))

def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)