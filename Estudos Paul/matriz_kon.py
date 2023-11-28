def criamatriz(a,b):
    
    matriz = []
    for i in range(a):
        linha = []
        for j in range(b):
           valor = int(input("Digite o elemento ["+str(i)+"]["+ str(j)+"]"))
           linha.append(valor)
        matriz.append(linha)
        

def le_matriz():
    lin = int(input("Digite o num de linhas: "))
    col = int(input("Digite o num de colunas: "))
    criamatriz (lin, col)

le_matriz()