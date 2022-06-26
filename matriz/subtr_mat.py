# Escrever um programa que recebe duas matrizes A e B
# e calcula a subtração de duas matrizes e mostra na tela.
# Criar uma função para preencher a matriz (preencher_matriz)
# e uma função para calcular a subtração (subtrair_matriz).


#função para a qntd de linhas
def lin ():
    x = int(input("Digite o número de linhas desejado: "))
    return x

#função para a qntd de colunas
def col ():
    y = int(input("Digite o número de colunas desejado: "))
    return y

#função para preencher matriz com as linhas e colunas como parametro
#a matriz será preenchida fixando as linhas e variado as colunas,
#ou seja, de forma horizontal
def preencher_mat(linha, coluna):
    #cria uma lista
    mat = []
    for i in range (linha):
        #cria uma lista para cada linha, a qual irá conter os elementos
        linha = []
        for j in range (coluna):
            #para cada coluna, um novo elemento na lista linha
            linha.append(int(input("Digite um número na posição %i %i da matriz: " %(i, j))))
        #antes de criar uma nova lista linha, a lista é adicionada à matriz na linha i
        mat.append(linha)
    print (mat)
    #retorna a matriz preenchida
    return mat

#função para subtrair duas matrizes de mesma ordem
#recebe as duas matrizes e suas respectivas linhas e colunas
def subtr_mat (mat1, mat2, linha1, coluna1, linha2, coluna2):
    #verifica se as matrizes recebidas são de mesma ordem
    if linha1 == linha2 and coluna1 == coluna2:
        #cria uma matriz que será preenchida com a subtração
        mat3 = []
        #preenche a matriz fixando as linhas e variando as colunas
        for i in range (linha_1):
            #cria uma lista linha3 para conter os elementos da subtração de cada coluna
            linha3 = []
            for j in range (coluna_1):
                #preenche a lista linha3 com a subtração de cada elemento da linha i e da coluna j
                #de cada matriz passada como parametro
                linha3.append(mat1[i][j] - mat2[i][j])
            #preenche a matriz com a lista linha 3
            mat3.append(linha3)
        #retona a matriz subtraída
        return mat3
    #se as matrizes não forem de mesma ordem
    else:
        #retorna erro
        return "As matrizes são de ordens diferentes, logo não podem ser subtraídas."


#chamada das funções para saber a qntd de linhas e colunas
#e preencher a matriz 1
linha_1 = lin()
coluna_1 = col()
mat_1 = preencher_mat(linha_1, coluna_1) 

#chamada das funções para saber a qntd de linhas e colunas
#e preencher a matriz 2
linha_2 = lin()
coluna_2 = col()
mat_2 = preencher_mat(linha_2, coluna_2)

#chamada da função para subtrair as matrizes 1 e 2
mat_3 = subtr_mat(mat_1, mat_2, linha_1, coluna_1, linha_2, coluna_2)
print (mat_3)