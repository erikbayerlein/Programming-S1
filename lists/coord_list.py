#A coordenação do curso de Ciência da Computação
#  deseja saber se existem alunos cursando,
#  simultaneamente, as disciplinas de Fundamentos de Programação (FUP)
#  e Cálculo I. Coloque os números das matrículas dos alunos
#  que cursam FUP em um vetor, 20 alunos. 
# Coloque os números das matrículas dos alunos que cursam Cálculo I em 1
#outro vetor, 40 alunos. Mostre o número das matrículas que aparecem nos dois vetores.

FuP = [0]*20
Calc = [0]*40
Fc = []

for i in range (20):
    n = int(input("Digite o número de matrícula do %iº aluno de FuP: " %(i+1)))
    while n <= 0:
        print ("Entrada inválida.")
        n = int(input("Digite o número de matrícula do %iº aluno de FuP: " %(i+1)))
    else:
        FuP[i] = n

for i in range (40):
    c = int(input("Digite o número de matrícula do %iº aluno de Cálculo: " %(i+1)))
    while c <= 0:
        print ("Entrada inválida.")
        c = int(input("Digite o número de matrícula do %iº aluno de Cálculo: " %(i+1)))
    else:
        Calc[i] = c

for i in FuP:
    for k in Calc:
        if i == k:
            Fc.append(i)

print ("As matrículas que aparecem nas duas turmas são: ", Fc)

