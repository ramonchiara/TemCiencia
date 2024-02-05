import random


class Familia:

    def __init__(self):
        self._meninos = 0
        self._meninas = 0

    def get_meninos(self):
        return self._meninos

    def get_meninas(self):
        return self._meninas

    def nasceu_menino(self):
        assert self.pode_ter_filhos()
        self._meninos += 1

    def nasceu_menina(self):
        assert self.pode_ter_filhos()
        self._meninas += 1

    def pode_ter_filhos(self):
        return self._meninos < 1

    def novo_nascimento(self):
        res = random.randint(0, 1)
        if res == 0:
            self.nasceu_menino()
        else:
            self.nasceu_menina()

    def simular(self):
        while self.pode_ter_filhos():
            self.novo_nascimento()
