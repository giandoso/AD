from math import log
from random import random

tempo_medio_clientes = 1.0 / 20  # 1.0 / tempo medio entre a chegada de clientes em segundos
tempo_medio_atendimento = 1.0 / 20
tempo = 0
tempo_simulacao = 5000


def minimo(a, b):
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

# armazena o somatorio do tempo ocupado do caixa
soma_atendimentos = 0.0
soma_areas = 0.0
soma_area_entrada = 0.0
soma_area_saida = 0.0
eventos_entrada = 0.0
eventos_saida = 0.0

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
        eventos_entrada += 1.0
        print(f'Fila: {fila}')
        # indica que o caixa esta ocioso
        # logo, pode-se comecar a atender
        # o cliente que acaba de chegar
        if saida_atendimento == 0.0:
            saida_atendimento = tempo

        # gera o tempo de chegada do proximo cliente
        tempo_anterior = chegada_cliente
        chegada_cliente = tempo + (-1.0/tempo_medio_clientes) * log(random())
        soma_areas += (chegada_cliente - tempo_anterior) * (fila - 1)
        soma_area_entrada += (chegada_cliente - tempo_anterior) * eventos_entrada

    else:
        # evento de saida de cliente
        # a cabeca da fila nao consiste no cliente em atendimento.
        # o cliente que começa a ser atendido portanto, sai da fila,
        # e passa a estar ainda no comercio, mas em atendimento no caixa
        if fila:
            fila -= 1.0
            eventos_saida += 1.0
            # tempo_anterior = tempo
            tempo_atendimento = -1.0/tempo_medio_atendimento * log(random())
            saida_atendimento = tempo + tempo_atendimento

            soma_atendimentos += tempo_atendimento
            soma_areas += (saida_atendimento - tempo) * (fila - 1)
            soma_area_saida += (saida_atendimento - tempo) * eventos_saida

            print(f'saida do cliente {saida_atendimento}')
            print(f'Fila: {fila}')

        else:
            tempo_ocioso = chegada_cliente - saida_atendimento
            print(f'Tempo ocioso: {tempo_ocioso}')
            # tempo_ocioso_total += tempo_ocioso
            saida_atendimento = 0.0
    print('----')

# trata problema de tempo de finalização
# o valor computado na iteração nao condiz com o fim da simulacao
if saida_atendimento > tempo:
    soma_atendimentos -= (saida_atendimento - tempo)
    soma_areas -= (saida_atendimento - tempo)


print(f'Taxa de utilização(%): {(soma_atendimentos / tempo) * 100}')
print(f'E[N]: {soma_areas/tempo}')
print(f'E[W]: {((soma_area_entrada - soma_area_saida) / eventos_entrada) / tempo}')