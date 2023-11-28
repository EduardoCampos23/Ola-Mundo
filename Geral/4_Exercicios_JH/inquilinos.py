# codando sistemas para casa de aluguel (John Alves)
#  4 listas principais.
inquilinos = []
pagamentos = []
pendentes = []
inadimplentes = []

geral = [inquilinos, pagamentos, pendentes, inadimplentes]

# Começo do meu laço e condicionais.

while True:
    cadastro_nome = input("Digite o nome do inquilino: ")
    if cadastro_nome == "consultar":
        print(f'Você tem {len(inquilinos)} inquilinos cadastrados ')
        print(f'Você tem {len(pagamentos)} pagamentos efetuados {pagamentos} ')
        print(f'Você tem {len(inadimplentes)} inquilinos inadimplentes: {inadimplentes} ')
    if cadastro_nome == "Baixa":
        print(pendentes)
        pg = input("Digite o nome do inquilino que será dado baixa: ")
        pagamentos.append(pg)
        print(f"Inquilinio adicionado a lista de baixas de pagamento {pagamentos}")
        pendentes.remove([pg])
        print(f"Clientes pendentes de pagamentos: {pendentes}")
        
        if cadastro_nome == "inadimplentes":
            print(f"Clientes pendentes de pagamentos {pendentes}")
            indp = input("Digite o nome do cliente inadimplente: ")
            pendentes.remove([indp])
            
            inadimplentes.append(indp)
            print("Cliente adicionado a lista de inadimplentes!")
            continue
    
    cpf = input("Digite o cpf: ")
    vencimento = int(input("Digite a data de vencimento: "))
    valor = float(input("Digite o valor do aluguel: "))
    casa = input("Digite qual a casa alugada: ")
    inquilino = [cadastro_nome, vencimento, valor, casa]        
    pg_pendente = [cadastro_nome]
    inquilinos.append(inquilino)
    pendentes.append(inquilino)
    pendentes.append(pg_pendente)
    print("Inquilino")

    if cadastro_nome == 'sair':

        print(geral)