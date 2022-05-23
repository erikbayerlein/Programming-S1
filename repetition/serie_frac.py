# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

n = int(input("Digite até que termo você gostaria de ir: "))

S = 0

for i in range (1, n + 1):
    k = i
    if i % 2 != 0:
        serie = (i + 1) / i
        print (serie)
        S += serie

print (S)
