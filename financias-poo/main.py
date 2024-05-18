from models.utilitarios import *

# Cadastrando Categorias 
categoria_salario = cadastrar_categoria(nome='Salario')
categoria_mesada = cadastrar_categoria(nome='Mesada')
categoria_lazer = cadastrar_categoria(nome='Lazer')
categoria_contas = cadastrar_categoria(nome='Contas mensais')

# Cadastrando Transação

cadastrar_transacao(
    descricao='Salario estágio OUT/2024',
    valor=320.25,
    categoria=categoria_salario
)
cadastrar_transacao(
    descricao='Mesada',
    valor=15.00,
    categoria=categoria_mesada
)
cadastrar_transacao(
    descricao='Lazer namorada - restaurantes 25/05/2024',
    valor=45.85,
    categoria=categoria_lazer
)
cadastrar_transacao(
    descricao='Conta de luz',
    valor=-225.41,
    categoria=categoria_contas
)

print(f'Saldo total final de R${saldo_total():.2f}')