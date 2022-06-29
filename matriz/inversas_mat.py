# Escreve um programa que recebe 2 matrizes (M e N) de números inteiros e
# verifica se ambas são inversas. Obs. A matriz inversa ocorre quando o
# produto de duas matrizes resulta numa matriz identidade de mesma ordem.

def preencher_mat (l, c):
    mat = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input("Digite o elemento da posição [%i][%i]: " %(i, j))))
        mat.append(linha)
    print(mat)
    return mat

def mult_matrizes (mat1, mat2, linha1, coluna1, linha2, coluna2):
    if coluna1 == linha2:
        mat_res = []
        for i in range(linha1):
            linha_res = []
            for j in range(coluna2):
                som = 0
                for k in range(linha2):
                    som += (mat1[i][k] * mat2[k][j])
                linha_res.append(som)
            mat_res.append(linha_res)
        print(mat_res)
        return mat_res
    else:
        return "Não é possível multiplicar as matrizes. Logo não são inversas."

def mat_inversa (mat):
    k = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                k += 1
            else: continue
    if k == len(mat):
        return "As matrizes são inversas."
    else:
        return "As matrizes não são inversas."


lin_1 = int(input("Digite o número de linhas da matriz 1: "))
col_1 = int(input("Digite o número de colunas da matriz 1: "))

lin_2 = int(input("Digite o número de linhas da matriz 2: "))
col_2 = int(input("Digite o número de colunas da matriz 2: "))

M = preencher_mat(lin_1, col_1)
N = preencher_mat(lin_2, col_2)

mn = mult_matrizes(M, N, lin_1, col_1, lin_2, col_2)

mat_i = mat_inversa(mn)
print(mat_i)