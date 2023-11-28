# aoa registrar uma venda, o cx da loja pergunta o nome , telefone e endereco e insere essa
# afirmacoes em uma aplicacao que ficara  executando durante o expediente da loja
# (ou seja em processo de repetiçao)

# a aplicacao guardara de alguma forma todas as ocorrencias  de cliente informados (Cabe a vc decidir como isso sera 
# armazenado) ate que o cx seja encerrado.
# ao final do expediente, o caixa ionforma um cliente chamdo fim. e a aplicacao sorteara  um dos clientes  atendidos 
#  ao longo do dia.
# a aplicacao informara na tela  todos os dados do cliente sorteado e se encerrara


contador = 0 #00

nome = input("Qual seu nome: ")
telefone = int(input("Qual sua idade: "))
endereço = input("Qual sua altura: ")

lista_clientes = [nome, telefone, endereço]

if nome == "fim":
    
    contador += 1
    
    print("___________________-----")
    print('Fim')
    

