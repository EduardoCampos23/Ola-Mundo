while True:

    numero_1 = input("digite um número:  ")         #INPUT DE DADOS
    numero_2 = input("digite outro número:  ")
    operador = input("digite um operador (+-/*): ")

    numeros_validos = None # isso é uma flag (bandeirinha)
    num_1_float = 0
    num_2_float = 0
                        
    try:  #para nao estourar uma execao - porem, má pratica de programação.
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None #ELE DIZ Q ISSO NAO É NECESSARI0, POREM USARÁ COMO FORMA DE PRECAUÇÃOb    
        if numeros_validos is None:
            print ('Um ou ambos os números digitados são inválidos.')
            continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    if operador == "+":
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    elif operador == "*":
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    elif operador == "/":
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
    elif operador == "-":
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
    else:
        print("não deveria chegar aqui.")

    sair = input ("Quer sair? [s]im: ").lower().startswith("s")
    
    if sair is True:
        break


#     nome  = input("Digite seu nome: ")
# altura = float(input("Digite sua altura: ")) 
# peso = float(input ("Digite seu peso: "))
# imc = peso / altura ** 2

# linha_1 = f'{nome} tem {altura} de altura,'
# linha_2 = f'pensa {peso} quilos e seu imc é'
# linha_3 = f'{imc}'

# print(linha_1)
# print(linha_2)
# print(imc)