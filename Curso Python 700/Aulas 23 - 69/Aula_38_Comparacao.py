primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

linha_1 = f"primeiro_valor = {primeiro_valor} é maior que segundo valor = {segundo_valor}"
linha_2 = f"segundo_valor  = {segundo_valor} é maior que primeiro valor = {primeiro_valor}"

if primeiro_valor > segundo_valor:
    print(linha_1)

elif segundo_valor > primeiro_valor:
    print (linha_2)


