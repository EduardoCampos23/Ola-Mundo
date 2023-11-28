
'''

entrada = input ('[E]ntrar [S]air:')
senha_digitada = input ('Senha: ')

senha_permitida = '123456'

if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')

else: 
    print('Sair')

    

'''

#if 1 and 1:
   # print(True and 1 and False)
    #Avaliacao de curto circuito

 #   senha = input ('Senha ') or 'Senha nao digitada'
#print (senha)


#Avaliacao de curto circuito

print (0 or False or 0 or 'abc' or True)