P = [0]*9
count = 0

for i in range (9):
    P[i] = int(input("Digite um número: "))

for n in P:
    if n % 2 != 0 and n % 3 != 0 and n != 1:
        print ("%i é um número primo." %(n))
        count += 1
    elif n == 2 or n == 3:
        print ("%i é um número primo." %(n))
        count += 1

print ("%i números primos." %(count))