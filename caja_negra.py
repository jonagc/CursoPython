""" Se basa en la especificacion de la funcioon o el programa

* Prueba de inputs y valida outputs.
*Unit testing o integrations testing
(Pruebas unitarias o pruebas integradas)
"""

import unittest #modulo que permite realizar pruebas en python

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):# test para ver que la funcion suma este correcta
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15) #Verifica si da 15 o no

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)
    
if __name__ == '__main__':
    unittest.main()

