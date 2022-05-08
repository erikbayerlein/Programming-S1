# Faça um programa que dado um número inteiro positivo (ℤ*+),
# calcule a soma de todos os números primos que existem até o número informado.

# Entrada do número inteiro
num = int(input("Digite um número: "))

# Contador para guardar a soma dos números primos
count_prim = 0

# Exluir todos os inteiros negativos, o zero e o 1, visto que não há como somar
# números primos digitando o valor 1
while num <= 0 or num == 1:
    num = int(input("Entrada inválida. Digite um número: "))

# Repetição de 1 até o número escolhio (+ 1 para excluir o zero)
for i in range (1,num + 1):
# If para incluir o 2 e o 3 na soma dos números primos
    if i / 2 == 1 or i / 3 == 1:
        count_prim += i  
# Elif para incluir todos os números que dividos por 2 e por 3 possuem resto diferente de 0
# e excluir o 1, ou seja, incluir todos os números primos - {2, 3} até %num
    elif i % 2 != 0 and i % 3 != 0 and i != 1:
        count_prim += i

# Dados de saída (a soma dos números primos até o número (num) escolhido)
print ("A soma dos números primos até %i é: %i" %(num,count_prim))
