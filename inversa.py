# Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

A = [0]*10
X = [0]*10

for i in range (10):
    A[i] = float(input("Digite um número: "))

print (A)

A.reverse()
print (A)