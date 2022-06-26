# Escreva um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
# a) o maior elemento da matriz e sua respectiva posição (linha e coluna);
# b) o menor elemento da matriz e sua respectiva posição.

#função para preencher matriz 6x3
def preencher_mat ():
    mat = []
    for i in range (6):
        linha = []
        for j in range (3):
            linha.append(int(input("Digite o elemento %i %i da matriz: " %(i, j))))
        mat.append(linha)
    print (mat)
    #retorna a matriz preenchida
    return mat

#função para verificar o maior elemento da matriz
#recebendo a matriz preenchida como parametro
def maior (mat):
    #variável para guardar o maior elemento da matriz recebe o primeiro elemento da matriz
    maior = mat [0][0]
    #percorrer a matriz
    for i in range (6):
        for j in range (3):
            #se maior for menor ou igual ao elemento da matriz, maior recebe o elemento
            if maior <= mat [i][j]:
                maior = mat [i][j]
                #salva a linha (i) na variavel maior_lin
                maior_lin = i
                #salva a coluna (j) na variavel maior_col
                maior_col = j
    #retorna o maior elemento, a sua linha e a sua coluna
    return maior, maior_lin, maior_col

#função para verificar o menor elemento da matriz
#recebendo a matriz preenchida como parametro
def menor (mat):
    #variável para guardar o menor elemento da matriz recebe o primeiro elemento da matriz
    menor = mat [0][0]
    for i in range (6):
        for j in range (3):
            #se menor for maior ou igual ao elemento da matriz, menor recebe o elemento
            if menor >= mat [i][j]:
                menor = mat [i][j]
                #salva a linha(i) do menor elemento
                menor_lin = i
                #salva a coluna(j) do menor elemento
                menor_col = j
    #retorna o menor elemento, a sua linha e a sua coluna
    return menor, menor_lin, menor_col

#chamada da função para preencher a matriz
mat = preencher_mat()
#chamada da função para verificar o maior elemento
#maior_el recebe maior, maior_linha recebe maior_lin e maior_coluna recebe maior_col
maior_el, maior_linha, maior_coluna = maior(mat)
#chamada da função para verificar o menor elemento
#menor_el recebe menor, menor_linha recebe menor_lin e menor_coluna recebe menor_col
menor_el, menor_linha, menor_coluna = menor(mat)
print ("O maior elemento da matriz é: %i e está em %i %i." %(maior_el, maior_linha, maior_coluna))
print ("O menor elemento da matriz é: %i e está em %i %i." %(menor_el, menor_linha, menor_coluna))