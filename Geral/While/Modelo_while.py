# d


#segundo codigo while


print("*** Operação de divisão ***")

while True:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    if n2 == 0:
        print("Divisor não pode ser 0.\nPrograma será encerrado...")
        break
    print(f"{n1} / {n2} = {(n1/n2):.2f}")

print("*** Fim da operação de divisão ***")