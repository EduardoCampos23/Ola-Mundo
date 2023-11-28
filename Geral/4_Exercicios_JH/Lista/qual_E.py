numeros = [ ]

for count in range(10):
 numeros += [count] #numero =numero + count
for count in numeros:
 print(count)


 ########################################33


 lista = [10, 20, 30]
lista.append(50)

listab = [10]

listac = lista + listab

listad = lista.extend(listab)
print(listad  )

