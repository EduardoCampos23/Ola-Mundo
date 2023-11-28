# 1°: Solicite um número ao usuário e mostre se o número é positivo, negativo ou se ele é 0. 
# Se o numero for positivo mostre se ele é impar ou par, se for negativo mostre o numero ao quadrado.
# numero = int(input("Digite um número: "))

# if  numero >= 1:
    
#     print("O número ", f"{numero}", "é positivo. ")
#     modulo = numero % 2 == 0

#     if modulo is True:
#         print("O numero é par.")

#     else:
#         print("O numero é impar.")

# elif numero == 0:
#     print("O numero", f"{numero}", "é zero.")

# elif numero <= -1:
#     quadrado = numero * numero 
#     print("O numero", f"{numero}", "é negativo e o seu quadrado é " f"{quadrado}."  )               

###############################################################################################333

# 2°: A cancela de um estabelecimento, em momento de pandemia, funciona dependendo da temperatura aferida e registrada pelo recepcionista do local. É preciso criar um algoritmo para liberar ou não a cancela dependendo da temperatura corporal. Com um medidor o recepcionista irá aferir e registrar no sistema e o algoritmo deverá liberar caso a temperatura seja <= 37 e não liberar caso a temperatura seja maior que 37º. A cancela só recebe True ou False (True para liberar e False para bloquear)

# # 3°: A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 
# grupos de indústrias que são altamente poluentes do meio ambiente. O índice de 
# poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias
# do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para
# 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades,
# se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas
# atividades. Faça um algoritmo que leia o índice de poluição medido e emita a
# notificação adequada aos diferentes grupos de empresas.

# # 4°:Ler o nome de 2 times e o número de gols marcados na partida (para cada time). 
# E no final escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a
# palavra EMPATE.

# 5°: Desenvolva um algoritmo que solicite o preço de três produtos e informe qual 
# produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.

# 6°: Uma empresa quer verificar se um empregado está qualificado para a aposentadoria 
# ou não. Para isso tem que se ter um dos seguintes requisitos:

# Ter no mínimo 65 anos de idade.
# Ter trabalhado no mínimo 30 anos.
# Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

# # Faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento
# e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de
#  trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'

# #Sou novata em Phyton e não sei criar todo o código exigido no enunciado. 
# Segue enunciado: Leia números inteiros do teclado até que um número negativo seja 
# 
# teclado. 
# Escreva, caso existam, quais os cinco maiores números lidos. Caso menos que cinco
#  números sejam lidos, mostre todos os números lidos. 
# Restrição Não é permitido manter em memória mais que seis números lidos.

#9. Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for
#  maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D forem
#  positivos e se A for par escrever a mensagem "Valores aceitos" senão escrever a
#  mensagem "Valores não aceitos"
# Valores aceitos = 2 3 2 6q  yç] 


############################################################################################################

#Exercício 6 livro python 
# 
#Construa um programa que tem como dados de entrada dois pontos quaisquer no plano cartesiano
#: P1 e P2. Considere que P1 é definido pelas coordenadas x1 e y1, enquanto P2 por x2, y2.
#O programa deve calcular e escrever a distância entre os pontos P1 e P2. A fórmula que calcula 
#A distâcia entre os dois pontos é dada por: 

#d = (x2 - x1)2 + (y2 - y1)2

#Para receber os daods de entrada, use as variáveis x1, y1, x2 e y2
# DIca a função que calcula a raiz quadrada de um número real é a sqrt (square root).
#Para usá-la, importe a da biblioteca math da seguinte forma: from math import sqrt.   

#solucao:

# abcissa_1 = int(input("Digite a abscissa x1: "))
# ordenada_1 = int(input("Digite a ordenada y2: "))

# x1 = abcissa_1
# y1 = ordenada_1


# abscissa_2 = int(input("Digite a abscissa x1: "))
# ordenada_2 = int(input("Digite a ordenada y2: "))

# x2 = abscissa_2
# y2 = ordenada_2

# x =(x2 - x1)**2 + (y2 - y1)**2

# from  math import sqrt
# print("A coodernada é: ", sqrt(x))

############################################
#Exercício Infinity School - 9
#  Leia 4 valores inteiros A, B, C e D. A seguir,
#  se B for maior do que C e se D for maior do que A,
#  e a soma de C com D for maior que a soma de A e B e se C e D forem positivos
#  e se A for par escrever a mensagem "Valores aceitos" senão escrever a mensagem
#  "Valores não aceitos"
# DIca de valores aceitos - 2 3 2 6

# 6. Considere uma equação do segundo grau, representada pela expressão
# ax2 + bx + c = 0
# Construa um programa no qual o usuário informe os valores das constantes a, b e c.
# Ao fim, o rpograma deve calcular e imprimir o valor de . Sabe-se que Delta =b2 - 4ac.

##############################################



