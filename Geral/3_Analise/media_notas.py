# # # # 4°: Faça um programa que receba várias notas e que calcule e 
# mostre a média das notas digitadas. Finalize escrevendo a nota igual a zero.


acumulado = 0
contagem = 0
nota = 1

while nota != 0:
    nota = float(input("Digite a nota: "))

    if nota != 0: 
        acumulado += nota
        contagem += 1

media = acumulado / contagem

print(f"A media total das notas foi: {media}")