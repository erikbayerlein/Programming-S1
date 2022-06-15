#  Faça um programa que receba N números inteiros
#  e mostre o maior número ímpar entre eles 
# (suponha que os números possam ser repetidos).
#  Se nenhum deles for ímpar, mostre uma mensagem constatando esse fato.

def imp(x, y):
    if x % 2 != 0 and y % 2 != 0:
        if x > y:
            return "x é ímpar e maior que y"
        elif x == y:
            return "x e y são ímpares e iguais"
        elif y > x:
            return "y é ímpar e maior que x"
    elif x % 2 == 0 or y % 2 == 0:
        if x % 2 != 0 and y % 2 == 0:
            return "x é o único ímpar"
        elif y % 2 != 0 and x % 2 == 0:
            return "y é o único ímpar"
        elif x % 2 == 0 and y % 2 == 0:
            return "x e y são pares"

num = int(input("Digite o número x: "))
num2 = int(input("Digite o número y: "))
print (num)
print (num2)

imp(num,num2)
result = imp(num,num2)
print (result)