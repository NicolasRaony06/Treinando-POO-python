from canecas.caneca import Caneca
from canecas.caneca_cafe import CanecaCafe

caneca1 = Caneca('cinza', 'plástico', '10x5')
caneca2 = Caneca('preta', 'plástico', '10x5')

print(caneca1.status)

caneca1.encher()
print(caneca1.status)

caneca1.beber()
print(caneca1.status)

print(caneca1.esta_cheia())

caneca3 = CanecaCafe('15h', 'doce/amargo', True)
caneca4 = CanecaCafe('8h', 'doce/amargo', False)

print(caneca3.is_cappucino())

print(caneca4.is_cappucino())

caneca3.encher()
print(caneca3.status)

caneca4.beber()
print(caneca4.status)

input()
