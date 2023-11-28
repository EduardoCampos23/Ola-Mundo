'''
CONSTANTE = "Variáveis que não vão mmudar
Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)    

'''

velocidade = 61 # velocidade atual do carro
local_carro = 98 #local em que o carro se encontra (KM)

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100
RADAR_RANGE = 1 # Distancia onde o radar pega

if velocidade > RADAR_1:
    print("Carro passou da velocidade do radar 1.")

if local_carro >= (LOCAL_1 - RADAR_RANGE ) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE ) and \
        velocidade > RADAR_1:
        print("carro multado em radar 1")
