
while True:

    n = 0
    count = 0
    lista = []

    while count <= n: 
        n = int(input("digite um numero: "))    
        if n %2 == 0:
            lista.append(n)

        count += 1     

    print(lista)