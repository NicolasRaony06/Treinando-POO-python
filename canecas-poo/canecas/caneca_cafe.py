from canecas.caneca import Caneca

class CanecaCafe(Caneca): #Herdando class Caneca
    def __init__(self, horario_cafe, sabor_cafe, leite_status):
        super().__init__("Amarela", "Porcelana", "13x4.2")
        self.horario_cafe = horario_cafe
        self.sabor = sabor_cafe
        self.leite_status = leite_status

    def is_cappucino(self):
        if self.leite_status:
            return True
        else:
            return False
