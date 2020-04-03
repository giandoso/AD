import math
import random

tempo_medio_clientes = 1.0 / 10  # arrumar
tempo_medio_atendimento = 1.0 / 8 # arrumar
tempo=0
tempo_simulacao=100000


def minimo(a, b):
    # b = 0.0 if b is None else b
    if a < b:
        return a
    else:
        return b


"""
COPIAR ENUNCIADO DA GRAVAÇÃO
"""
# armazena o tempo de chegada do proximo cliente
chegada_cliente = (-1.0/tempo_medio_clientes) * math.log(random.random())


# armazena o tempo em que o cliente que estiver em atendimento saira do comercio
# saida_atendimento == 0.0 indica caixa ocioso
saida_atendimento = 0.0
fila = 0.0


# logica da simulacao
while(tempo < tempo_simulacao):
    # nao existe cliente sendo atendido no momento atual,
    # de modo que a simulacao pode avancar no tempo para
    # a chegada do proximo cliente
    if(saida_atendimento == 0.0):
        tempo = chegada_cliente
    else:
        tempo = minimo(chegada_cliente, saida_atendimento)


    if(tempo == chegada_cliente):
        print(f'Chegada do cliente {chegada_cliente}')
        # evento de chegada de cliente
        fila = fila + 1.0
        print(f'Fila: {fila}')
        # indica que o caixa esta ocioso
        # logo, pode-se comecar a atender
        # o cliente que acaba de chegar
        if(saida_atendimento == 0.0):
            saida_atendimento = tempo


        # gera o tempo de chegada do proximo cliente
        chegada_cliente = tempo + ((-1.0/tempo_medio_clientes) * math.log(random.random()))
        # TODO gerar tempo de chegada do proximo cliente
    else:
        # evento de saida de cliente
        # a cabeca da fila nao consiste no cliente em atendimento.
        # o cliente que começa a ser atendido portanto, sai da fila,
        # e passa a estar ainda no comercio, mas em atendimento no caixa
        if(fila):
            fila = fila - 1.0
            saida_atendimento = tempo + ((-1.0/tempo_medio_atendimento) * math.log(random.random()))
            print(f'saida do cliente {saida_atendimento}')
            print(f'Fila: {fila}')
        else:
            saida_atendimento = 0.0
            print(f'Caixa ocioso até {chegada_cliente}')
    print('----')


