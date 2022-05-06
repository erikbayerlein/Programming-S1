# Faça um programa que leia 5 números e informe o maior número

maior_num = 0

for i in range (0, 5):
    num = int(input("Digite um número: "))
    while num > maior_num: 
        maior_num = num

print ("O maior número que você digitou foi: %i" %(maior_num))
