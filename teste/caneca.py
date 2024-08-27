import json

class Caneca:
    status = 0
    
    def __init__(self, nome, volume, formato, tema):
        self.nome = nome
        self.volume = volume
        self.formato = formato
        self.tema = tema

    def encher_caneca(self):
        self.status = 1

    def all(self):
        return {
            'nome':self.nome, 
            'volume':self.volume, 
            'fomato':self.formato, 
            'tema':self.tema,
            'status':'vázia' if not self.status else 'cheia'
            }
    
    values = []
    def salvar(self):
        canecas_dir = r'./POO/canecas.json'
        self.values.append(self.all())
        canecas_json_object = json.dumps(self.values, indent=4)
        
        with open(canecas_dir, 'a', encoding='utf-8') as canecas:
            canecas.write(canecas_json_object)
            canecas.close()
        return canecas_dir
