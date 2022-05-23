# Faça um programa usando listas que recebe a nota dos alunos de uma turma e
#  calcula a média aritmética da turma não tendo como
#  pré- conhecimento da quantidade de alunos da turma.
# Observações
#  Entrada: O usuário deve digitar como entrada a nota de cada aluno (nota >=0)
#  Saída: O algoritmo deve imprimir a média da turma
#  O valor da média deve ter duas casas decimais,
#  use a formatação com o caractere % vista no início da aula.

count = 0
g = 0
x = 0
A = [0]*1000

while True:
    A[count] = float(input("Digite a nota do %iº aluno: " %(count+1)))
    x = A[count]
    if x < 0 or x > 10:
        break
    g += A[count]
    count += 1

media = g / count

print (media)
