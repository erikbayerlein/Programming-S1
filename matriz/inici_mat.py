mat = []
mat2 = []
mat3 = []

def preencher_mat(x, y):
    mat = []
    for i in range (x):
        linha = []
        for j in range (y):
            linha.append(int(input("Digite o elemento da matriz: ")))
        mat.append(linha)
    print (mat)
    return mat

def mult_mat(m1, m2, l1, c2):
    result = 0
    mat_3 = []
    for i in range (l1):
        for j in range (c2):
            for k in range (l1):
                result += m1[i][j] * m2[i][j]
                mat_3.append(result)
    return mat_3




linhas_1 = int(input("Digite a quantidade de linhas da matriz 1: "))
colunas_1 = int(input("Digite a quantidade de colunas da matriz 1: "))

linhas_2 = int(input("Digite a quantidade de linhas da matriz 2: "))
colunas_2 = int(input("Digite a quantidade de colunas da matriz 2: "))

mat1 = preencher_mat(linhas_1, colunas_1)
mat2 = preencher_mat(linhas_2, colunas_2)

if colunas_1 == linhas_2:
    mat3 = mult_mat(mat1, mat2, linhas_1, colunas_2)
    print (mat3)
    