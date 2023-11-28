cpf = '74682489070'
nove_dig = cpf[:9]
cont_regresssivo = 10


resultado_dig1 = 0
for digito in nove_dig:
    resultado_dig1 += int(digito) * cont_regresssivo
    
    cont_regresssivo -= 1

digito1 = ((resultado_dig1*10) % 11)
digito1 = digito1 if digito1 <= 9 else 0 