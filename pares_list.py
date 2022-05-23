A = [0]*10
P = [0]*10
I = [0]*10

j = 0
k = 0
count_p = 0
count_i = 0

for l in range (10):
    A[l] = int(input("Digite um número."))

for i in A:
    if i % 2 == 0:
        P [k] = i
        k += 1

        count_p += 1
        print ("O número %i é par" %(i))
        
    else:
        I [j] = i
        j += 1

        count_i += 1
        print ("O número %i é ímpar" %(i))

print ("A quantidade de números pares é: %i" %(count_p))
print ("A quantidade de números ímpares é: %i" %(count_i))

print (P)
print (I)