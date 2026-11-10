"""
Case 4: Controle e Dosagem de Tanques de Fluidos (Batelada)
Automação de Processos Químicos, Alimentos e Saneamento
"""

import random
import time

linhas = 4   # número de tanques
colunas = 3  # número de sensores de pH por tanque

faixa_min = 6.5 #margem pH
faixa_max = 7.5 #margem pH


def coletar_ph_tanques(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha_sensores = []
        for j in range(colunas):

            valor_ph = round(random.uniform(5.5, 8.5), 2)
            linha_sensores.append(valor_ph)
        matriz.append(linha_sensores)
    return matriz


def validar_lotes(matriz):
    vetor_status = []
    medias = []
    for x in matriz:
        media = sum(x) / len(x) #calcula a média
        if faixa_min <= media <= faixa_max:
          status = 1
        else:
          status = 0
        vetor_status.append(status)
        medias.append(media)
    return vetor_status, medias


def acionar_valvulas_escoamento(vetor_status):
    acoes = []
    for status in vetor_status:
        if status == 1:
            acoes.append("Abrir Válvula de Escoamento")
        else:
            acoes.append("Disparar Alarme Químico")

    return acoes


while True:
    matriz_ph = coletar_ph_tanques(linhas, colunas)
    vetor_status, medias = validar_lotes(matriz_ph)
    acoes = acionar_valvulas_escoamento(vetor_status)

    for i in range(linhas):
        if vetor_status[i] == 1:
            situacao = "LIBERADO (pH na faixa ideal)"
        else:
            if medias[i] < faixa_min:
                situacao = "RETIDO (Muito Ácido)"
            else:
                situacao = "RETIDO (Muito Alcalino)"

        print(f"Tanque {i + 1}: pH {medias[i]:.2f} | {situacao} | {acoes[i]}")
    time.sleep(20)
