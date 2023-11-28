# # ##Retornando o indice de um elemento pg 119.

# # atrizes = ['adriana padro', 'barbara borges', 'camila queiroz', 'danielle winits']
           
# # procurar_por = "camila queiroz"

# # if procurar_por in atrizes:
# #     indice = atrizes.index(procurar_por)

# #     print(f'{procurar_por} esta no indice {indice}')

# # else: 
# #     print(f'{procurar_por} nao esta na lista')


# ################################################################################

# # # Retornando indice e elemento. pg 123


# atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda","oi"]    
    

# for indice, nome in enumerate(atrizes):
#     print(indice, nome)

# ########################################################
           
 
# retorna indice Otavio 

# lista = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda","oi"]    
# # indice = enumerate(lista)

# for x in enumerate(lista):
#     print("------")

#     for item in x:
#         print(item)


import random
atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
"Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
"Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
random.shuffle(atrizes) #Embaralha a lista
print(f"Lista embaralhada: {atrizes}")
sorteada = random.choice(atrizes) #Sorteia aleatoriamente
print(F"Atriz sorteada: {sorteada}")