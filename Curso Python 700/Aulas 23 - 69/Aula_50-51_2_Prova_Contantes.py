

"""velocidade = 60 # velocidade atual do carro
local_carro = 100 #local em que o carro se encontra (KM)

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100
RADAR_RANGE = 0.1 # Distancia onde o radar pega


velocidade_permitida = velocidade <= 60

velocidade_para_infracao = velocidade > RADAR_1

Faixa_do_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <=(LOCAL_1 + RADAR_RANGE)

carro_fora_do_radar = local_carro != LOCAL_1"""

ano  = 2021
print(ano)
ano  = 2023
print(ano)








































"""if velocidade_para_infracao and Faixa_do_radar:
    print("Carro multado.")

else:
     print("Carro abaixo da velocidade de multa ou fora do radar, não será multado")"""


