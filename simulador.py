from math import log
from random import random

tempo_medio_clientes = 1.0 / 0.25  # 1.0 / tempo medio entre a chegada de clientes em segundos
tempo_medio_atendimento = 1.0 / 0.15
tempo = 0
tempo_simulacao = 100000


def minimo(a, b):
    # b = 0.0 if b is None else b
    if a < b:
        return a
    else:
        return b


"""
 Simulador de um caixa onde clientes cheguem em média a cada 10 segundos,
 e o caixa gaste em média 8 segundos para atender cada cliente.
 
 Utilização ou Ocupação = fração de tempo que o caixa permanecerá ocupado.
 Utilização = 0.8.
 
 o tempo entre a chegada de clientes, bem como o tempo de atendimento devem 
 ser gerados de maneira pseudoaleatoria através da v.a. exponencial.
"""
# armazena o tempo de chegada do proximo cliente
chegada_cliente = (-1.0/tempo_medio_clientes) * log(random())

# armazena o somatorio do tempo ocioso do caixa
tempo_ocioso_total = 0.0

# armazena o tempo em que o cliente que estiver em atendimento saira do comercio
saida_atendimento = 0.0
fila = 0.0


# logica da simulacao
while tempo < tempo_simulacao:
    # nao existe cliente sendo atendido no momento atual,
    # de modo que a simulacao pode avancar no tempo para
    # a chegada do proximo cliente
    # saida_atendimento == 0.0 indica caixa ocioso
    if saida_atendimento == 0.0:
        tempo = chegada_cliente
    else:
        tempo = minimo(chegada_cliente, saida_atendimento)

    if tempo == chegada_cliente:
        print(f'Chegada do cliente {chegada_cliente}')
        # evento de chegada de cliente
        fila += 1.0
        print(f'Fila: {fila}')
        # indica que o caixa esta ocioso
        # logo, pode-se comecar a atender
        # o cliente que acaba de chegar
        if saida_atendimento == 0.0:
            saida_atendimento = tempo

        # gera o tempo de chegada do proximo cliente
        chegada_cliente = tempo + (-1.0/tempo_medio_clientes) * log(random())
    else:
        # evento de saida de cliente
        # a cabeca da fila nao consiste no cliente em atendimento.
        # o cliente que começa a ser atendido portanto, sai da fila,
        # e passa a estar ainda no comercio, mas em atendimento no caixa
        if fila:
            fila -= 1.0
            saida_atendimento = tempo + (-1.0/tempo_medio_atendimento) * log(random())
            print(f'saida do cliente {saida_atendimento}')
            print(f'Fila: {fila}')

        else:
            tempo_ocioso = chegada_cliente - saida_atendimento
            print(f'Tempo ocioso: {tempo_ocioso}')
            tempo_ocioso_total += tempo_ocioso
            saida_atendimento = 0.0
    print('----')


tempo_ocupado_total = tempo - tempo_ocioso_total
taxa_utilizacao = tempo_ocupado_total / tempo
print(f'Tempo ocioso total: {tempo_ocioso_total}')
print(f'Tempo ocupado total: {tempo_ocupado_total}')

print(f'Taxa de utilização(%): {taxa_utilizacao * 100}')
