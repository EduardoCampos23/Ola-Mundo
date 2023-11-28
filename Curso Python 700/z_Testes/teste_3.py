cpf  = '74682489070'
nove_dig = cpf[:9]
cont_regressivo = 10

for numero in nove_dig:
    print(numero, cont_regressivo)
    cont_regressivo -=1