#Usando a estrutura PARA, 
#peça para o usuário entrar com um número inteiro
# maior que zero e calcule o fatorial desse número.

import math

num = int(input("Digite um número: "))

while num <= 0:
    num = int(input("Entrada inválida, digite outro número: "))

fact = math.factorial(num)

print ("O fatorial do número digitado é: %i" %(fact))