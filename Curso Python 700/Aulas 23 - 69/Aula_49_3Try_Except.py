
numero_str = input ('Vou dobrar o numero que vc digitar:')

try:
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_str)
    print (f"O dobro de {numero_str} é {numero_float *2}")

except:
    print( "Isso não é um numero.")