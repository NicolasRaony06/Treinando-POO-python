class Conjunto:
    def __init__(self, elementos):
        if type(elementos) == list:
            self.elementos = elementos
        else:
            self.elementos = []
            print("Os elementos do conjuntos devem estar em formato de lista!")

    def numero_elementos(self):
        return len(self.elementos)
    
    def esta_contido(self, conjunto):
        if conjunto.numero_elementos() < self.numero_elementos():
            return False
        
        verified = 0
        for elemento in self.elementos:
            if elemento in conjunto.elementos:
                verified += 1

        if verified == len(self.elementos):
            return True
        
        else: return False
            

    def __str__(self):
        return f"Conjunto de elementos: {self.elementos}"
    
    # def __int__(self, valor):
    #     self.elementos 

    
