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


if __name__ == '__main__':
    N = 10000
    sociedade = [Familia() for _ in range(0, N)]
    for f in sociedade:
        f.simular()

    # questão 1
    meninas = sum([f.get_meninas() for f in sociedade])
    meninos = sum([f.get_meninos() for f in sociedade])
    proporcao = meninas / meninos
    print(f'Proporção entre meninas e meninos = {meninas}:{meninos} = {proporcao:.1f}')

    # questão 2
    media = (meninos + meninas) / N
    print(f'Média de filhos por família = {media:.1f}')
