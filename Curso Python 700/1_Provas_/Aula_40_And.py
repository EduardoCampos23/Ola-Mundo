#Operadores Lógicos
# and (e) or (ou) not (não)
# And todas as condições precisam ser verdadeiras.
# Se qualuqer valor for falso a expressão inteira sera
# avaliada naquele valor.
# São consideradas falsy (que vc ja viu)
# 0 0,0 "" False
#Tambem existe o tipo none que é
# usado para representar um não valor
# entrada = input ('[E]entrar [S]air)


entrada = input ('[E]ntrar [S]air:')
senha_digitada = input ('Senha: ')

senha_permitida = '123456'

if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')

elif entrada == "S":

    print('Voce deseja realmente sair')

else: 
    print('Sair')

    

