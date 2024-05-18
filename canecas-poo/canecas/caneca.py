class Caneca:
    formato = 'Cilindrico'

    def __init__(self, cor, material, tamanho):
        self.cor = cor
        self.material = material
        self.tamanho = tamanho
        self.status = 'vázia'

    def encher(self):
        self.status = 'cheia'

    def beber(self):
        self.status = 'vázia'

    def esta_cheia(self):
        if self.status == 'vázia':
            return False
        else:
            return True