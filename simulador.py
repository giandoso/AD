from math import log
from random import random

# case 1
# tempo_medio_clientes, tempo_medio_atendimento = 1.0 / 0.25, 1.0 / 0.15

# case 2
# tempo_medio_clientes, tempo_medio_atendimento = 1.0 / 2, 1.0 / 1.6

# case 3
tempo_medio_clientes, tempo_medio_atendimento = 1.0 / 0.5, 1.0 / 0.45

# case 4
# tempo_medio_clientes, tempo_medio_atendimento = 1.0 / 3, 1.0 / 2.97


tempo = 0
tempo_simulacao = 10000


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

numero_eventos = 0.0
soma_areas = 0.0
tempo_anterior = 0.0


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
        chegada_cliente = tempo + (-1.0/tempo_medio_clientes) * log(random())

        # calculo do E[N]
        soma_areas += (tempo - tempo_anterior) * numero_eventos
        tempo_anterior = tempo
        numero_eventos += 1

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

            print(f'saida do cliente {saida_atendimento}')
            print(f'Fila: {fila}')

        else:
            saida_atendimento = 0.0

        # calculo do E[N]
        if tempo_anterior < tempo:
            soma_areas += (tempo - tempo_anterior) * numero_eventos
            tempo_anterior = tempo
            numero_eventos -= 1

        soma_area_saida += (saida_atendimento - tempo) * eventos_saida

    print('----')

# trata problema de tempo de finalização
# o valor computado na iteração nao condiz com o fim da simulacao
if saida_atendimento > tempo:
    soma_atendimentos -= (saida_atendimento - tempo)
    soma_areas -= (saida_atendimento - tempo)

# soma_areas += (tempo - tempo_anterior) * numero_eventos

U = ((soma_atendimentos / tempo) * 100)
L = soma_areas/tempo
W = (soma_area_entrada - soma_area_saida) / eventos_entrada
_lambda = eventos_entrada/tempo

# print_mode = 1  # small
print_mode = 2  # details

if print_mode == 1:
    print(f'{U}\t{L}\t{W}\t{_lambda}'.replace('.', ','))
else:
    print(f'Taxa de utilização(%): {U:.4f}')
    print(f'                    L: {L:.4f}')
    print(f'                    W: {W:.4f}')
    print(f'               lambda: {_lambda:.4f}')

print(f'Validação de little: {abs(L - _lambda * W)}')