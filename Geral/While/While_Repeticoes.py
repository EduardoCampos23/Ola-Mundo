
senha_salva = "1234"
senha_digit = " "
repeticoes = 1

while senha_salva != senha_digit:
    senha_digit = input(f"Sua senha({repeticoes}x):")

    repeticoes += 1

print(f'Voce teve {repeticoes - 1} tentativas.')
