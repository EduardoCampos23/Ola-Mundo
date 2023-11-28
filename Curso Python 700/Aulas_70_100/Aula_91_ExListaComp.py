import os

lista = []

while True:
    print("Selecione uma opcao: ")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system("cls")
        
        Produto  = input("Valor: ")
        lista.append(Produto)

    elif opcao == "a":
        indice_str= input("Digite um indice para apagar: ")

        try:
            indice = indice_str
            del lista[indice]

        except ValueError:
            print("Digite um int.")

        except IndexError:
            print("Digite um indice valido.")

        except Exception:
            print('Erro dessconhecido.')

    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')         
                       


