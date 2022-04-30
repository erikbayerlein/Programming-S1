# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 == n2 and n1 == n3:
    print ("Os números são iguais.")

elif n1 >= n2 and n1 >= n3 and n2 >= n3:
    print ("O maior número é: ", n1,". E o menor número é: ", n3)
elif n1 >= n2 and n1 >= n3 and n3 >= n2:
    print ("O maior número é: ", n1,". E o menor número é: ", n2)

elif n2 >= n1 and n2 >= n3 and n1 >= n3:
    print ("O maior número é: ", n2,". E o menor número é: ", n3)
elif n2 >= n1 and n2 >= n3 and n3 >= n1:
    print ("O maior número é: ", n2,". E o menor número é: ", n1)

elif n3 >= n1 and n3 >= n2 and n2 >= n1:
    print ("O maior número é: ", n3,". E o menor número é: ", n1)
elif n3 >= n1 and n3 >= n2 and n1 >= n2:
    print ("O maior número é: ", n3,". E o menor número é: ", n2)