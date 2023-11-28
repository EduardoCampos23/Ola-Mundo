'''
Operadores de recebimento
= += -= *= /= //= **= %=

contador = 0

while contador <= 10:
    contador = contador + 1 
    print(contador)

print("Acabou")    

'''
contador = 0

while contador <= 100:
    contador += 1 

    if contador == 8:
        print("oi")   
        continue

    if contador >= 10 and contador <= 27:
        continue

    # if contador >= 10 and contador <= 27:
    #   print("Não vou mostrar o", contador)    
    # continue
    

    print(contador)   
         
   
print("Acabou")    

