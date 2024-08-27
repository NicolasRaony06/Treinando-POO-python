from caneca import Caneca

# batman_caneca = Caneca(
#     nome='Batman',
#     volume='250ml',
#     formato='cilindrico',
#     tema='super-heróis'
# )

# print(batman_caneca.all())

# batman_caneca.encher_caneca()

# print(batman_caneca.all())

# batman_caneca.salvar()
import json
path = r'./POO/canecas.json'
def read_json(path):

    f = open(path)

    data = json.load(f)                 #utilizar essa função read_json para dar load nos objetos anteriores

    print(type(data))






