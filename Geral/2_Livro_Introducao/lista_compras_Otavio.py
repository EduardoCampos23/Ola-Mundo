lista = []



while True:
    count = 0

    entrada = input('[i]inserir,[a]apagar,[l]listar: ')

    if entrada == "i":
        produto = input("Digite um produto: ")
  
        
        for item, iteracao in enumerate(lista):   
            lista.append(produto)
            print(item,iteracao)

    if entrada == "a":
        r = input("Digite o indice: ")
        if r == item:
            lista.pop(item)

    count +=1

# else: 
#     print("____________________end")
#     pass
    print(lista)

 