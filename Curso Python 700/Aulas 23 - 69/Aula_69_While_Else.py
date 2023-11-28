# While / Else


frase = "O Python é uma longuagem de programação " \
"multiparadigma."\
"Python foi criado por Guido van Rossum."

#print(frase.count("Phyton"))
string = "Valor Qualquer"

i = 0
while i < len(string):
    letra = string[i]

    if letra == " ":
        break

    print(letra)
    i += 1

else:
    print("Não encontri um espaco na string.")

print("Fora do Else.")  