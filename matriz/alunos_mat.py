# Faça um programa que preencha uma matriz 6 × 3
# com as notas de seis alunos em três provas.
# O programa deverá mostrar um relatório com
# o número dos alunos (número da linha) e a prova
# em que cada aluno obteve menor nota. 
# Ao final do relatório, deverá mostrar quantos alunos
# tiveram menor nota em cada uma das provas: 
# na prova 1, na prova 2 e na prova 3.

#função para preencher matriz 6x3
def preencher_mat():
    mat = []
    for i in range (6):
        linha = []
        for j in range (3):
            linha.append(int(input("Digite a nota do aluno %i na prova %i: " %(i+1, j+1))))
        mat.append(linha)
    #retorna a matriz preenchida
    return mat

#função para verificar a menor nota do aluno(i) em cada prova(colunas)
def menor_nota_def (mat, aluno):
    #recebe a primeira nota do aluno(i) na prova 1 (coluna 0)
    menor = mat [aluno][0]
    #fixa as linhas (i) e varia as colunas
    for j in range (3):
        #se menor for maior ou igual à nota de determinada coluna
        if menor >= mat [aluno][j]:
            #menor receber a nota
            menor = mat [aluno][j]
            #salva a coluna(prova) em que a nota está 
            coluna = j
    #retorna a nota e a coluna(prova)
    return menor, coluna

#chamada da função para preencher a matriz
notas = preencher_mat()
print (notas)

#criação de contadores para cada prova
prova_1 = 0
prova_2 = 0
prova_3 = 0


for i in range (6):
    #chamada da função para percorrer a matriz e verificar a melhor nota
    #passando a matriz e o número da linha/aluno (i) como parametro
    #menor_nota recebe menor e prova recebe coluna
    menor_nota, prova = menor_nota_def(notas, i)
    #i+1 para a corrigir o número do aluno (linha)
    #prova+1 para corrigir o número da prova (coluna)
    print ("A menor nota do aluno %i foi: %i na prova %i" %(i+1, menor_nota, prova+1))
    #contador para contar quantos alunos com a menor nota em cada prova
    #prova começa com 0, pois indica a coluna da matriz
    if prova == 0:
        prova_1 += 1
    elif prova == 1:
        prova_2 += 1
    elif prova == 2:
        prova_3 += 1

#print dos contadores de cada prova
print ("%i alunos com a menor nota na prova 1" %prova_1)
print ("%i alunos com a menor nota na prova 2" %prova_2)
print ("%i alunos com a menor nota na prova 3" %prova_3)