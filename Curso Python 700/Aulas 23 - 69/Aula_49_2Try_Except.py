numero_str = input ('Vou dobrar o numero que vc digitar:')

if numero_str.isdigit():

    numero_float = float(numero_str)
    print (f"O dobro de {numero_str} é {numero_float *2}")

else:

    print("Isso não é um numero.")
