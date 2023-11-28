# # # from random import randrange
# # # import random
 
# # # linhas = int(input("Número de linhas: "))
# # # colunas = int(input("Número de colunas: "))
 
# # # A = [[randrange(1, 11)  for i in range(colunas)]
# # #                         for j in range(linhas)]


# # # # B = [[randrange(1, 11)  for i in range(colunas)]
# # # #                         for j in range(linhas)


# # # print(A)     

# # var = 0

# # for x in range(7):
# #    var += 1
# # print(vmatriz

# def cria_matriz(num_linhas, num_colunas,valor):

#    matriz  = []
#    for i in range(num_linhas):
#          linha = []
#          for j in range(num_colunas):
#             linha.append(linha)

# #######################3333

# provavelmente exe do jonh = identificar


# # # # # # # # #####################################################################################################
# # # # # # # # # 3. Uma turma de formandos está vendendo rifas para angariar 
# # # # # # # # # recursos financeiros para sua cerimônia de formatura. Construa 
# # # # # # # # um programa para cadastrar os nomes das pessoas que 
# # # # # # # # # compraram a rifa. Ao fim, o programa deve sortear o ganhador 
# # # # # # # # # do prêmio e imprimir o seu nome.

# # # # # # # import random
 
# # # # # # # atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
# # # # # # #  "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
# # # # # # #  "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
 
# # # # # # #  # Embaralha elementos
# # # # # # # random.shuffle(atrizes)
# # # # # # #  # Ordena elem entos crescentemente
# # # # # # # atrizes.sort() # mesmo que usar atrizes.sort(reverse = False)
# # # # # # # print(atrizes)
# # # # # # #  # Ordena elementos decrescentemente
# # # # # # # atrizes.sort(reverse = True)
# # # # # # # print(atrizes)



# # # # # # nadadores = ["Paulo", "Roberto", "Antonio", "João", "Manoel", "Eduardo", "Cassio"]
# # # # # # tempos = []
# # # # # # nadadorTempo = []
# # # # # # for x in nadadores:
# # # # # #     n = int(input(f"Digite o tempo do nadador {x}: "))
# # # # # #     tempos.append(n)
# # # # # #     nadadorTempo.append(x)
# # # # # #     nadadorTempo.append(n)
# # # # # # else:
# # # # # #     indiceDoMelhorTempo = tempos.index(min(tempos))
# # # # # #     indiceDoPiorTempo = tempos.index(max(tempos))
# # # # # #     melhorTempo = tempos[indiceDoMelhorTempo]
# # # # # #     piorTempo = tempos[indiceDoPiorTempo]
# # # # # #     mediaTempo = sum(tempos)/len(tempos)
# # # # # #     indice = tempos.index(min(tempos))
# # # # # #     print(f"O pior tempo foi do nadador {nadadores[indiceDoPiorTempo]}: {piorTempo} segundos")
# # # # # #     print(f"O melhor tempo foi do nadador {nadadores[indiceDoMelhorTempo]}: {melhorTempo} segundos")
# # # # # #     print(f"E a média de tempo foi de {int(mediaTempo)} segundos")



# # # # # # lista = [1,2,3,4,5,6,7,8,9]
# # # # # lista = ["a","b","c","d"]

# # # # # lista.sort(reverse = True)

# # # # # print(lista)

# # # # atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
# # # # "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
# # # # "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
 
# # # # backup = list(atrizes)
 
# # # # # Verifica se a cópia é igual à original
# # # # if backup == atrizes:
# # # #         atrizes.clear()
# # # #         print("Lista de atrizes esvaziada")
# # # # else:
# # # #         print("ERRO: Cópia gerada não é igual à original")


# # # atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda"]
# # # atrizes_internacionais = ["Angelina", "Viola"]
 
# # # atrizes.extend(atrizes_internacionais)
 
# # # print(atrizes)


# # atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda"]
 
# # for indice, nome in enumerate(atrizes):
# #   #  print(f"{nome} está armazenado no índice {indice}")
# #     print(indice, nome)

# lista1 = [x ** 2 for x in range(10)]
# print(lista1)

# lista2 = []
# lista2 = [x for x in range(1,20) if x % 2 == 0]
# print(lista2)

# lista3 = [i for i in "HACKATHON" if i in ["A","E","I","O","U"]] 
# print(lista3)

# lista4 = [1,2,3]
# lista4 = [i**3 for i in lista4]
# print(i)