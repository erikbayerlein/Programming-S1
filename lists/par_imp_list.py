# Faça um Programa que leia 20 números inteiros e armazene- os em uma lista. 
# Armazene os números pares na lista
# PAR e os números IMPARES na lista impar. Imprima as três listas.

A = [0]*20
P = []
I = []

for i in range (20):
    A[i] = int(input("Digite o %iº número: " %(i + 1)))

for i in range (20):
    if A[i] % 2 == 0:
        P.append(A[i])
    else:
        I.append(A[i])

print (A)
print (P)
print (I)