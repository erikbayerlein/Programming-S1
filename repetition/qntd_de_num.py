countp = 0
counti = 0

for i in range (1,11):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        countp = countp + 1
    else:
        counti = counti +1

print ("A quantidade de números pares é: %i \
    \nA quantidade de números ímpares é :%i " % (countp, counti))
