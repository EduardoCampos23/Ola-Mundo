
# def cria_matriz(num_linhas, num_colunas, valor):

#         matriz = []   
        

#         for i in range(num_linhas):
#                 linha = []
#                 for j in range(num_colunas):
#                         linha.append(valor)
                
#         matriz.append(linha)

#         return matriz

# cria_matriz(4,4,0)
num_linhas  = int(input("linhas: "))
num_colunas = int(input("colunas: "))
valor = int(input("valor: "))


matriz = []   
        
        
for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
                linha.append(valor)
                
        matriz.append(linha)

print (matriz)
