class Familia:

    def __init__(self):
        self._meninos = 0
        self._meninas = 0
        self._pode_ter_filhos = True

    def get_meninos(self):
        return self._meninos

    def get_meninas(self):
        return self._meninas

    def nasceu_menino(self):
        self._meninos += 1
        self._pode_ter_filhos = False

    def nasceu_menina(self):
        self._meninas += 1

    def pode_ter_filhos(self):
        return self._pode_ter_filhos
