nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
altura = float(input("Qual sua altura: "))
peso = float(input("Qual seu peso: "))

op= int(input("Estado civil:\n1.1 - Casado\n2.2 - Solteiro\n"))

if op==1:
    op = True
else:
    op = False

eu = [nome, idade, altura, peso, op]

print("_____________________")
print("Nome  : ", eu[0])
print("Idade : ", eu[1], " anos")
print("Altura: ", eu[2], "m")
print("Peso  : ", eu[3], "kg")
print("Casado: ", eu[4])