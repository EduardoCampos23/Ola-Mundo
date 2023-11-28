

def calculo(*arg):

    produto = 10
    for x in arg:
        produto -= x 
    
    return produto


z= calculo(1,2,3,4,5,6,7,8,9,1)
print(z)

# paz = True if vencer_o_thanos else False
# tipo_de_x = "Par" if x % 2 == 0 else "impar