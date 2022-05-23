# Faça um programa que receba como entrada um inteiro positivo (ℤ*+ ) n,
#  que vai indicar até onde a seguinte série finaliza: 1/1 + 1/2 + 1/3 + ... + 1/n.
# Dado o valor 'n' e a soma dos valores que compõem a série,
#  seu objetivo é calcular a soma dos termos da série onde os denominadores são pares.

# Dados de entrada (até que número deseja ser somado)
num = int(input())

# Contador para os denominadores pares
count_par = 0

# Caso o usuário digite números negativos ou 0
while num <= 0:
    num = int(input())

# Somar todos as razões com denominadores i's pares até o número escolhido
for i in range (1, num + 1):
    if i % 2 == 0:
        serie = 1/i
        count_par += serie

# Dado de saída
print (count_par)