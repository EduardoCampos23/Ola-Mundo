'''
Iterável -> str, range, etc...
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
inter -> me entregue seu iterador

'''

# texto = iter("Luiz") #___iter___()

# print(texto)
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

#################################3
# texto = iter("Luiz") #___iter___()

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# ################################
# uso do for:

# texto = "Luiz"
# for letra in texto:
#     print(letra)

# como o for funciona: o codigo abaixo e a forma detalhada do cod acima:

texto = "Luiz"  #iteravel
iterador = iter(texto) #iterador


while True:
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
       break                    


