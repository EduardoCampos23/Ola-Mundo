# # # 1°: Faça um programa que leia 3 números e informe o maior número.

# # # 2°: Desenvolva um gerador de tabuada, capaz de gerar uma tabuada de SOMA de 
# qualquer número inteiro entre 1 a 10. O usuário deve informar qual número deseja 
# ver a tabuada.

# # # 3°: Faça um programa que leia 5 números e informe a soma e a média dos números.

# # # # 4°: Faça um programa que receba várias notas e que calcule e mostre a média das notas
# # #  digitadas. Finalize escrevendo a nota igual a zero.

# # ## 5°: Faça um programa que receba 10 números entre 0 e 100 e usando laços de repetição
#   calcule e mostre a quantidade de números entre 25 e 75.

# # ## 6°: Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de 
#  repetição.

# ####7° 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
# mensagem caso o valor seja inválido e continue pedindo até que o usuário 
# informe um valor válido.

# # # Desafio: Faça um programa que obtenha a altura de um triângulo em um número 
# inteiro e imprima-o utilizando asteriscos. Veja o Exemplo:
# # Entrada: 5
# # *
# # **
# # ***
# # ****
# # *****

# ######################################################################################333


# # 1°: Faça um programa que leia 3 números e informe o maior número.

# numMaior = 0

# for i in range(3):
#     num = float(input("Digite um numero qualquer: "))

#     if num > numMaior:
#         numMaior = num

# print(f"O maior numero é igual a: {numMaior}")

# print("=========================")

# contador = 0
# numMaior = 0

# while contador < 3:
#     num = float(input("Digite um numero qualquer: "))

#     if num > numMaior:
#         numMaior = num
#     contador += 1

# print(f"O maior numero é igual a: {numMaior}")
# ##########################################################################################3

# Questão 2:

# num = int(input("Digite um numero de 1 a 10 para mostrar a tabuada 
# de soma: "))

# for i in range(1, 11):
#     soma = num + i

#     print(f"{num} + {i} = {soma}")

# print("====================")

# contador = 1

# while contador <= 10:
#     soma = num + contador

#     print(f"{num} + {contador} = {soma}")

#     contador += 1

# ###########################################################################

# Questão 3:

# acumulado = 0

# for i in range(5):
#     num = float(input("Digite um numero qualquer: "))

#     acumulado += num

# media = acumulado / 5

# print(f"A soma de todos os numeros foi: {acumulado}\n" +
# f"E a media foi: {media}")

# print("================")

# acumulado = 0
# contador = 0

# while contador < 5:
#     num = float(input("Digite um numero qualquer: "))

#     acumulado += num
# M7
#     contador += 1

# media = acumulado / 5

# print(f"A soma de todos os numeros foi: {acumulado}\n" +
# f"E a media foi: {media}")

# ##################################################################33

# Questão 4:


# acumulado = 0
# contagem = 0
# nota = 1

# while nota != 0:
#     nota = float(input("Digite a nota: "))

#     if nota != 0: 
#         acumulado += nota
#         contagem += 1

# media = acumulado / contagem

# print(f"A media total das notas foi: {media}")

# ########################################################################

# Questão 5:

# contagem = 0

# for i in range(10):
#     num = int(input("Digite um numero qualquer: "))

#     if 25 < num < 75:
#         contagem += 1

# print(f"O total de numeros entre 0 e 75 foram: {contagem}")

# print("===================")

# contagem = 0
# contador = 0

# while contador < 10:
#     num = int(input("Digite um numero qualquer: "))

#     if 25 < num < 75:
#         contagem += 1
    
#     contador += 1

# print(f"O total de numeros entre 0 e 75 foram: {contagem}")

# ######################################################################

# Questão 6:

# # 6°: Faça um programa que mostre as tabuadas dos números de 1 a 10
# #  usando laços de repetição.

# for i in range(1, 11):

#     for j in range(1, 11):
#         mult = i * j

#         print(f"{i} * {j} = {mult}")
    
#     print("________________________________")

# print("=============================")

# x = 1
# y = 1

# while x <= 10:

#     while y <= 10:
#         mult = x * y

#         print(f"{x} * {y} = {mult}")
        
#         y += 1
    
#     x += 1
#     y = 1
    
#     print("________________________________")

# ###########################################################################

# desafio:


# tam = int(input("Digite o tamanho do triangulo: "))

# lado = 1

# for i in range(tam):
    
#     for j in range(lado):
#         print("*", end=" ")

#     print()
    
#     lado += 1

# print("===============================")

# lado = 1
# x = 0
# y = 0

# while x < tam:

#     while y < lado:
#         print("*", end=" ")
#         y += 1
    
#     print()
    
#     lado += 1
#     y = 0
#     x += 1


#############################################3
# #7° 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
# mensagem caso o valor seja inválido e continue pedindo até que o usuário 
# informe um valor válido.

# while True:
#     

#     nota = int(input ("Digite uma nota de zero a dez: "))

#     if nota < 11:
#         print(f"sua nota é: {nota}")
#         break
    
#     if nota >= 11:    
       
#     