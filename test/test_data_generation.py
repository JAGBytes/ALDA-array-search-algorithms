import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from data import data_generator
from data import constants

class DataGeneratorTest(unittest.TestCase):
    def test_get_random_list_empty(self):
        # Si se pide una lista de tamaño 0, debe devolver una lista vacía.
        random_list = data_generator.get_random_list(0)
        self.assertEqual(len(random_list), 0)

    def test_get_random_list_length(self):
        # Verifica que para distintos tamaños, la lista generada tenga la longitud correcta
        for size in [1, 2, 10, 100]:
            random_list = data_generator.get_random_list(size)
            self.assertEqual(len(random_list), size)
            # Comprueba que cada número esté en el rango [0, MAX_VALUE]
            for number in random_list:
                self.assertGreaterEqual(number, 0)
                self.assertLessEqual(number, constants.MAX_VALUE)

    def test_get_random_x(self):
        # Ejecuta varias veces la función para verificar que el valor esté en el rango [1, MAX_VALUE]
        for _ in range(100):
            x = data_generator.get_random_x()
            self.assertGreaterEqual(x, 1)
            self.assertLessEqual(x, constants.MAX_VALUE)

if __name__ == '__main__':
    unittest.main(verbosity=2)
