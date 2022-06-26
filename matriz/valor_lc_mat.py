#Os alunos turma de Fundamentos de Programação do curso de Ciência da computação da UFC
# começaram a trabalhar com matrizes. Eles estão fazendo um algoritmo para descobrir a 
# linha da matriz de maior valor e a coluna da matriz de maior valor.
# Sendo que o valor de uma linha é calculado pela soma dos quadrados dos seus elementos,
# e o valor da coluna é calculado pela soma dos seus elementos. Faça um algoritmo que:
#a) Receba a ordem de uma matriz (nxm) e preencha essa matriz com dados de entrada fornecidos pelo usuário;
#b) Calcule e retorne a linha de maior valor e a coluna de maior valor;

#Obs. Manipular os dados obrigatoriamente usando matriz e pode utilizar os métodos de listas e strings.

#Entrada
#  A ordem da matriz: n quantidade de linhas e m quantidade de colunas
#  Os elementos da matriz (números inteiros)

#Saída
# A linha de maior valor e a coluna de maior valor

#EXEMPLO:
#Na matriz 2x2 abaixo:
#[[a1, a2], [a3, a4]]
#O valor da linha 0 é calculado por a1^2 + a2^2 O valor da coluna 0 é calculado por a1 + a3
#E assim sucessivamente.

def ordem_mat ():
    n = int(input("Digite a quantidade de linhas para a matriz: "))
    m = int(input("Digite a quantidade de colunas para a matriz: "))
    return n, m

def preencher_mat (linha, coluna):
    mat = []
    for i in range (linha):
        linha = []
        for j in range (coluna):
            linha.append(int(input("Digite o elemento para a posição %i %i: " %(i, j))))
        mat.append(linha)
    print (mat)
    return mat

def maior_linha (mat, linha, coluna):
    maior = 0
    som = 0
    m_linha = 0
    for i in range (linha):
        for j in range (coluna):
            som += mat [i][j]**2
        if maior <= som:
            m_linha = i
            maior = som
        som = 0
    return maior, m_linha

def maior_coluna (mat, linha, coluna):
    maior = 0
    som = 0
    m_coluna = 0
    for j in range (coluna):
        for i in range (linha):
            som += mat [i][j]
        if maior <= som:
            m_coluna = j
            maior = som
        som = 0
    return maior, m_coluna

linha, coluna = ordem_mat()
mat = preencher_mat(linha, coluna)

linha_valor, linha_maior = maior_linha(mat, linha, coluna)
coluna_valor, coluna_maior = maior_coluna(mat, linha, coluna)

print ("A linha de maior valor é %i de valor %i." %(linha_maior, linha_valor))
print ("A coluna de maior valor é %i de valor %i." %(coluna_maior, coluna_valor))