import random

import matplotlib.pyplot as plt
import pandas as pd


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

    # gráficos
    df = pd.DataFrame({
        'Familias': [i for i in range(1, N + 1)],
        'Meninas': [f.get_meninas() for f in sociedade],
        'Meninos': [f.get_meninos() for f in sociedade],
    })
    df['Filhos'] = df['Meninas'] + df['Meninos']
    df['Filhos Acc'] = df['Filhos'].cumsum()
    df['Média'] = df['Filhos Acc'] / df['Familias']

    # Famílias x Meninos e Famílias x Meninas
    df.plot(kind='scatter', x='Familias', y='Meninos').set_ylim(bottom=-1, top=df['Meninas'].max()+1)
    df.plot(kind='scatter', x='Familias', y='Meninas').set_ylim(bottom=-1, top=df['Meninas'].max()+1)
    plt.show()

    # Histograma para a quantidade de meninas
    df.plot(kind='hist', column='Meninas', bins=df['Meninas'].max())
    plt.show()

    # Famílias x Média de Filhos
    df.plot(kind='line', x='Familias', y='Média')
    plt.axhline(y=2, color='red', linestyle='dashed', label='Média esperada')
    plt.show()
