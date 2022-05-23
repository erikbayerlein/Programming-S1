# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range (1,6):
    num = float(input("Digite um número: "))
    soma += num

media = soma / 5

print ("A soma é: %i" %(soma))
print ("A média é: %i" %(media))
