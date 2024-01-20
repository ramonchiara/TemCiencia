import unittest

from ditador import Familia


class DitadorTest(unittest.TestCase):

    def setUp(self):
        self.f = Familia()

    def test_nova_familia_nao_tem_filhos(self):
        self.assertEqual(0, self.f.get_meninos())
        self.assertEqual(0, self.f.get_meninas())

    def test_ao_nascer_menino_o_numero_de_meninos_deve_aumentar(self):
        self.f.nasceu_menino()
        self.assertEqual(1, self.f.get_meninos())
        self.assertEqual(0, self.f.get_meninas())
