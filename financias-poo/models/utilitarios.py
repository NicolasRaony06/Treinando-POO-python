from models.categoria import Categoria
from models.transacao import Transacao

LISTA_TRANCACOES = []
LISTA_CATEGORIAS = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(
        nome = nome
    )

    LISTA_CATEGORIAS.append(nova_categoria)

    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(
        descricao=descricao,
        valor=valor,
        categoria = categoria
    )

    LISTA_TRANCACOES.append(nova_transacao)

    return nova_transacao

def saldo_total():
    saldo_total = 0
    for transacao in LISTA_TRANCACOES:
        saldo_total += transacao.valor
    
    return saldo_total