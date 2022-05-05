n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

s = n1 + n2 + n3

if n1 < n2 and n1 < n3:
    print ("O menor número digitado foi:", n1)
elif n2 < n1 and n2 < n3:
    print ("O menor número digitado foi:", n2)
else:
    print ("O menor número digitado foi:", n3)

if n1 > n2 and n1 > n3:
    print ("O maior número digitado foi:", n1)
elif n2 > n1 and n2 > n3:
    print ("O maior número digitado foi:", n2)
else:
    print ("O maior número digitado foi:", n3)

print ("A soma dos números digitados foi:", s)