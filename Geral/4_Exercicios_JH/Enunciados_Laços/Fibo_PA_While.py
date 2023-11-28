# n = int(input("Que termo deseja encontrar: "))

# ultimo = 1
# penultimo = 1

# if (n==1) or (n==2):
#     print("1")
# else:
#     count=3
#     while count <= n:
#         termo = ultimo + penultimo
#         penultimo = ultimo
#         ultimo = termo
#         count += 1
# print(termo)


# PA3
# #Um professor de Matematica deseja contruir um programa para gerar uma PA. Tres parametros 
# a) primeiro termo, b) quant de termos c) razao dessa PA. Construa uma programa para carregar e imprimir
# uma lista contendo os termos da PA, bem como a soma dos elementos da PA>

inicial = int(input(':'))
quant = int(input(':'))
r = int(input(':'))

count=0

while count <= quant:
        lista = []

        x = inicial + r
        x = inicial
        lista.append(x)
        count += 1
        
print(lista)        