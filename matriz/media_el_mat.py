# Preencher uma matriz 2x2 com números de entrada do
# usuário e calcular a média dos elementos dessa matriz.


#função para preencher matriz 2x2
#fixando as linhas e preenchendo as colunas
def preencher_mat2x2 ():
    #cria a matriz
    mat = []
    for i in range (2):
        #cria uma lista linha, a qual irá conter os elementos da linha i
        linha = []
        for j in range (2):
            #preenche a lista linha de acordo com a qntd de colunas
            linha.append(int(input("Digite o elemento %i %i da matriz: " %(i, j))))
        #preenche a linha i da matriz
        mat.append(linha)
    print (mat)
    #retorna a matriz preenchida
    return mat

#função para calcular a media dos elementos de uma matriz
#matriz preenchida como parametro
def media_elementos (mat):
    #inicialização da variável para conter a soma final de todos os elementos
    som = 0
    for i in range (2):
        for j in range (2):
            # cada elemento da linha i e coluna j é somado à soma
            som += mat[i][j]
    #cálculo da média
    media = som/4
    #retona a média das somas
    return media

#chamada da função para preencher a matriz
mat = preencher_mat2x2()
#chamada da função para calcular a média dos elementos
#passando a matriz como parametro
media = media_elementos(mat)
print ("A média dos elementos é: %i" %media)