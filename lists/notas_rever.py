# Faça um programa que receba as notas de 20 alunos
#  e armazena-as em uma lista, 
# após isso o seu programa deve:
# a) Ordenar a lista de notas em ordem decrescente
#  (sem a usar o sort, sorted ou métodos de ordenação) e imprimi-la.

A = [0]*20

for i in range (20):
    n = int(input("Digite a nota do %iº alunos: " %(i + 1)))
    while n < 0 or n > 10:
        print ("Entrada inválida.")
        n = int(input("Digite a nota do %iº alunos: " %(i + 1)))
    else:
        A[i] = n

