lista1 = []
lista2 = []

while True:
    n = int(input("Digite um número lista 1: "))
    if n < 0 or n > 100:
        print ("Entrada inválida")
        break
    lista1.append(n)

while True:
    n = int(input("Digite um número para a lista 2: "))
    if n < 0 or n > 100:
        print ("Entrada inválida")
        break
    lista2.append(n)

i = 0
pos = 0
tam1 = len(lista1)
tam2 = len(lista2)
lista_intercala = []

while i < tam1:
    lista_intercala.append(lista1[i])
    lista_intercala.append(lista2[i])
    i += 1
    pos = i

for i in range (pos, tam2):
    lista_intercala.append([i])

print (lista_intercala)