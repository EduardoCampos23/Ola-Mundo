# # 3. Uma turma de formandos está vendendo rifas para angariar 
# # recursos financeiros para sua cerimônia de formatura. 
# Construa um programa para cadastrar os nomes das pessoas que 
# # compraram a rifa. Ao fim, o programa deve sortear o ganhador 
# # do prêmio e imprimir o seu nome.

import random



listaDeParticipantes = []



while True:
   
    cadastro = input("Digite o nome do participante ou digite 'Fim' para concluir: ").upper()
    if cadastro == "FIM":
        ganhador = random.choice(listaDeParticipantes)
        print(f"O ganhador foi {ganhador}")
        break
        
    
    listaDeParticipantes.append(cadastro)
    print(listaDeParticipantes)

        
        