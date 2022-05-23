# Faça um programa (notas_lista.py) que recebe a média de 5 alunos, 
# calcula a média da turma, e mostrar a posição na lista e a nota dos alunos
# que ficaram de AF (4 <= nota < 7).
# 1. Recebe a nota dos 5 alunos
# 2. Calcula a média da turma
# 3. Mostra a nota dos alunos de AF e suas posições na lista

N = [0]*5
m = 0

for i in range (5):
    N[i] = float(input("Digite a nota do %dº aluno: " %(i+1)))
    while N[i] < 0 or N[i] > 10:
        print ("Entrada inválida.")
        N[i] = float(input("Digite novamente a nota do aluno: "))
    m += N[i]

media = m / 5
print ("A média da turma é : %.2f" %media)

print (N)

for i in range (5):
    if N[i] < 7 and N[i] >= 4:
        print ("O aluno da posição %i da turma ficou de AF com nota: %.2f" %(i+1, N[i]))

# A = sorted(N)

# print (A)

# for i in range (5):
    # if A[i] < 7 and A[i] >= 4:
        # print ("O aluno da posição %i da turma ficou de AF com nota: %.2f" %(i+1, A[i]))