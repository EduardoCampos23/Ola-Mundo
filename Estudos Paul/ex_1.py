# 7. Crie um programa que gere, aleatoriamente, uma matriz M, 
# com elementos no intervalo [0, 1]. A quantidade de linhas e de 
# colunas de M devem ser informadas pelo usuário. Ao fim, o 
# programa deve informar se M é uma matriz nula.

from random import randrange

n_linhas = int(input("Digite o numero de linhas: "))    
n_colunas = int(input("Digite o numero de colunas: "))
matriz = []
linha = []
    
def gmatriz():
    
    for l in range(n_linhas):
        linha = []
        matriz.append(linha)

        for c in range(n_colunas):
                coluna = randrange(0,2) 
                linha.append(coluna)
    printmatriz()    
                    
def printmatriz():

    for i in range(n_linhas):
        print(linha)       

            
    # if 1 in matriz: 
    #     print("matriz nula")
                    
gmatriz()         

        