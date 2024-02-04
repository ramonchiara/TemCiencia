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

    def test_ao_nascer_menina_o_numero_de_meninas_deve_aumentar(self):
        self.f.nasceu_menina()
        self.assertEqual(0, self.f.get_meninos())
        self.assertEqual(1, self.f.get_meninas())

    def test_nova_familia_pode_ter_filhos(self):
        self.assertEqual(True, self.f.pode_ter_filhos())

    def test_ao_nascer_menino_familia_nao_pode_mais_ter_filhos(self):
        self.f.nasceu_menino()
        self.assertEqual(False, self.f.pode_ter_filhos())

    def test_ao_nascer_menina_familia_continua_podendo_ter_mais_filhos(self):
        self.f.nasceu_menina()
        self.assertEqual(True, self.f.pode_ter_filhos())

    def test_apos_nascer_menino_deve_lancar_excecao_se_nascer_outro_menino(self):
        self.f.nasceu_menino()
        self.assertRaises(AssertionError, self.f.nasceu_menino)

    def test_apos_nascer_menino_deve_lancar_excecao_se_nascer_uma_menina(self):
        self.f.nasceu_menino()
        self.assertRaises(AssertionError, self.f.nasceu_menina)
