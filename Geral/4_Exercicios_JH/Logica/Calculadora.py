# 1°: Solicite um número ao usuário e mostre se o número é positivo, 
#negativo ou se ele é 0. 
# Se o numero for positivo mostre se ele é impar ou par, 
#se for negativo mostre o numero ao quadrado.

numero = int(input("Digite um numero:  "))

if numero >= 1:
    
    print ('O numero', f'{numero}', 'é positivo.')
    modulo_num_par = numero % 2 == 0 

    if modulo_num_par:
        print("O numero é par.")

    else:
        print("O numero é impar.")

elif numero == 0:
    print ('O numero', f'{numero}', 'é zero.')

elif numero <= -1:
    quadrado = numero * numero
    print ('O numero', f'{numero}', 'é negativo e seu quadrado é 'f'{quadrado}.')

else: 
     
    print("Você não digitou um numero.")