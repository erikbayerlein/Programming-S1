lin_mat1 = int(input("Digite o número de linhas da matriz 1: "))
col_mat1 = int(input("Digite o número de colunas da matriz 1: "))

lin_mat2 = int(input("Digite o número de linhas da matriz 2: "))
col_mat2 = int(input("Digite o número de colunas da matriz 2: "))

mat1 = []
mat2 = []

for i in range(lin_mat1):
    linha1 = []
    for j in range(col_mat1):
        linha1.append(int(input("Digite um elemento para a M[%i][%i]: " %(i,j))))
    mat1.append(linha1)
print (mat1)

for i in range(lin_mat2):
    linha2 = []
    for j in range(col_mat2):
        linha2.append(int(input("Digite um elemento para a M[%i][%i]: " %(i,j))))
    mat2.append(linha2)
print (mat2)

if col_mat1 == lin_mat2:
    mat_mult = []
    for i in range(lin_mat1):
        linha3 = []
        for j in range (col_mat2):
            mult = 0
            for k in range (lin_mat2):
                mult += (mat1[i][k] * mat2[k][j])
            linha3.append(mult)
        mat_mult.append(linha3)    
    print (mat_mult)

else:
    print("Eu dou o cu")