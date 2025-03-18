import sys
import os
# Se agrega la ruta raíz del proyecto para que se puedan importar correctamente los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from algorithms import binary_search, jump_search, linear_search

class SearchAlgorithmsTests(unittest.TestCase):
    
    def test_linear_search(self):
        # En linear_search no es necesario que el array esté ordenado.
        test_cases = [
            # (array, target, se espera encontrar el target)
            ([3, 1, 4, 2, 5], 4, True),
            ([3, 1, 4, 2, 5], 6, False),
            ([], 1, False),
            ([1, 1, 2, 3], 1, True),
            ([10, 20, 30, 40], 10, True),
        ]
        for arr, target, exists in test_cases:
            result = linear_search.linear_search(arr, target)
            if exists:
                self.assertNotEqual(result, -1, f"Se esperaba encontrar {target} en {arr}")
                self.assertEqual(arr[result], target, f"El índice retornado no corresponde al target en {arr}")
            else:
                self.assertEqual(result, -1, f"Se esperaba no encontrar {target} en {arr}")
    
    def test_binary_search(self):
        # binary_search requiere arrays ordenados.
        test_cases = [
            ([1, 2, 3, 4, 5], 3, True),
            ([1, 2, 3, 4, 5], 6, False),
            ([], 1, False),
            ([1, 1, 2, 3], 1, True),
            ([10, 20, 30, 40], 10, True),
        ]
        for arr, target, exists in test_cases:
            result = binary_search.binary_search(arr, target)
            if exists:
                self.assertNotEqual(result, -1, f"Se esperaba encontrar {target} en {arr}")
                self.assertEqual(arr[result], target, f"El índice retornado no corresponde al target en {arr}")
            else:
                self.assertEqual(result, -1, f"Se esperaba no encontrar {target} en {arr}")
    
    def test_jump_search(self):
        # jump_search también requiere arrays ordenados.
        test_cases = [
            ([1, 2, 3, 4, 5], 3, True),
            ([1, 2, 3, 4, 5], 6, False),
            ([], 1, False),
            ([1, 1, 2, 3], 1, True),
            ([10, 20, 30, 40], 40, True),
        ]
        for arr, target, exists in test_cases:
            result = jump_search.jump_search(arr, target)
            if exists:
                self.assertNotEqual(result, -1, f"Se esperaba encontrar {target} en {arr}")
                self.assertEqual(arr[result], target, f"El índice retornado no corresponde al target en {arr}")
            else:
                self.assertEqual(result, -1, f"Se esperaba no encontrar {target} en {arr}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
