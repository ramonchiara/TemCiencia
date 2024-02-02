class Familia:

    def __init__(self):
        self.meninos = 0
        self.meninas = 0
        self._pode_ter_filhos = True

    def get_meninos(self):
        return self.meninos

    def get_meninas(self):
        return self.meninas

    def nasceu_menino(self):
        self.meninos += 1
        self._pode_ter_filhos = False

    def nasceu_menina(self):
        self.meninas += 1

    def pode_ter_filhos(self):
        return self._pode_ter_filhos
