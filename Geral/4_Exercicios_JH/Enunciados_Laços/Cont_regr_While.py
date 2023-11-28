# 1 - Escreva um programa que solicite ao usuário um número inteiro positivo
# e realize uma contagem regressiva a partir desse número até zero,
# imprimindo cada número no processo.


n = int(input("Digite um número inteiro positivo: "))

count = 0
print(n)
x = n


while count < x:
  
    n_1 = n - 1
    novo_n = n_1
    n = novo_n
    
    print(novo_n)    

    count+=1