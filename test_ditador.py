import unittest

from ditador import Familia


class DitadorTest(unittest.TestCase):

    def test_nova_familia_nao_tem_filhos(self):
        f = Familia()
        self.assertEqual(0, f.get_meninos())
        self.assertEqual(0, f.get_meninas())
