convidados = []

count = 1

for i in range(3):
    nome_convidados = input("Digite o nome do convidado: ")
    convidados.append((nome_convidados,count))
    count += 1
    
print('Estes são os convidados: ')
for nome, numero in convidados:

 print(f'Convidado: {numero} {nome}')
