# def multi(x,*arg):

#     def dobr():
#         a = x * 2
#         return a
    
#     def impr():
#         lista = []
#         for t in arg:
#             lista.append(t)
#         return lista

#     def quad():
#         c = x * 4
#         return c
    
#     return dobr(), impr(), quad()

# h= (multi(2, 2,5,4))

# print(h)


######################3
# exer do otavio

def calcular(m):#2

    def multiplicando(n):    
        return m * n
             
    def somando(n):
        return n + m 
         
    return multiplicando, somando

dupl = calcular(2)
# soma = calcular(1)

lista = []
t = (dupl[1](31))
u = (dupl[0](7))

lista.append(t)
lista.append(u)
print(lista)




# print(soma(2))
