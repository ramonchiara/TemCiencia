class Familia:

    def __init__(self):
        self.meninos = 0

    def get_meninos(self):
        return self.meninos

    def get_meninas(self):
        return 0

    def nasceu_menino(self):
        self.meninos += 1
