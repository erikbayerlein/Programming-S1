# calcular o determinante de uma matriz quadrada 2x2

def preencher_mat(ordem):
    mat = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(int(input("Digite o elemento [%i][%i]: " %(i, j))))
        mat.append(linha)
    print(mat)
    return mat

def calc_det(mat, ordem):
    if ordem == 1:
        determ = mat[0][0]
        return determ
    else:
        determ = (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
        return determ

while True:
    ordem = int(input("Digite a ordem da matriz: "))
    if ordem <= 0:
        print("Entrada inválida. Tente novamente.")
    else:
        break

mat = preencher_mat(ordem)
det = calc_det (mat, ordem)
print ("O determinante da matriz é: %i" %det)