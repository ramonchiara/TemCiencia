class Familia:

    def __init__(self):
        self.meninos = 0
        self.meninas = 0

    def get_meninos(self):
        return self.meninos

    def get_meninas(self):
        return self.meninas

    def nasceu_menino(self):
        self.meninos += 1

    def nasceu_menina(self):
        self.meninas += 1

    def pode_ter_filhos(self):
        return True
