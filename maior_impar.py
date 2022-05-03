# Faça um programa (maior_impar.py) que receba três números inteiros e mostre o maior número ímpar entre eles 
# (suponha que os números sejam diferentes). Se nenhum deles for ímpar, mostre uma mensagem constatando esse fato. 
# Teste o seu programa com as seguintes entradas:
# 2, 4, 5
#  7, 8, 4
#  4, 6, 3 
# 4, 6, 2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

impar1 = num1 % 2
impar2 = num2 % 2
impar3 = num3 % 2

maior_num = 0

if impar1 == 0 and impar2 == 0 and impar3 ==0:
    print ("Todos os números são pares.")

else:
    # quando o numero 1 e o numero 2 forem impares
    if impar1 != 0 and impar2 != 0 and impar3 == 0:
        if num1 > num2:
            print ("O maior número ímpar é: %i" %(num1))
        elif num2 > num1:
            print ("O maior número ímpar é: %i" %(num2))
    # quando o numero 1 e o numero 3 forem impares
    elif impar1 != 0 and impar3 != 0 and impar2 == 0:
        if num1 > num3:
            print ("O maior número ímpar é: %i" %(num1))
        elif num3 > num1:
            print ("O maior número ímpar é: %i" %(num3))
    # quando o numero 2 e o numero 3 forem impares
    elif impar2 != 0 and impar3 != 0 and impar1 == 0:
        if num2 > num3:
            print ("O maior número ímpar é: %i" %(num2))
        elif num3 > num2:
            print ("O maior número ímpar é: %i" %(num3))
    # quando todos os numeros forem impares
    elif impar1 != 0 and impar2 != 0 and impar3 != 0:
        if num1 > num2 and num1 > num3:
            maior_num = num1
        elif num3 > num1 and num3 > num2:
            maior_num = num3
        elif num2 > num1 and num2 > num3:
            maior_num = num2
        print ("O maior número ímpar é: %i" %(maior_num))
    #quando o apenas o numero 1 for impar
    elif impar1 != 0:
        print ("O maior número ímpar é: %i" %(num1))
    #quando o apenas o numero 2 for impar
    elif impar2 != 0:
        print ("O maior número ímpar é: %i" %(num2))
    #quando o apenas o numero 3 for impar
    elif impar3 != 0:
        print ("O maior número ímpar é: %i" %(num3))
