import json

class Caneca:
    ID = None
    status = 0
    PATH = r'canecas.json'

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
    
    def read_json(self):
        pass
        

    values = []
    def salvar(self):
        try:
            json_file = open(self.PATH)
            data = json.load(json_file)
        except:
            data = None
        
        if data:
            data.append(self.all())
        else:
            data = []
            data.append(self.all())

        canecas_json_object = json.dumps(data, indent=4)
        with open(self.PATH, 'w', encoding="utf-8") as canecas:
            canecas.write(canecas_json_object)
            canecas.close()

        return self.PATH
