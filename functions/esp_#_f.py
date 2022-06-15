# Faça uma função que recebe uma frase e substitui todas as
# ocorrências de espaço por “#”. Faça também uma função para
# realizar a entrada de dados. A saída de dados deve ser feita no programa principal.

def subst(x):
    #transform a string em lista para poder ser alterada
    x_list = list(x)
    #estrutura de repetição para a alteração da lista
    for i in range (len(x_list)):
        # cada espaço encontrado será substituído por uma #
        if x_list[i] == " ":
            x_list.pop(i)
            x_list.insert(i, "#")
    #transforma a lista em string
    frase2 = "".join(x_list)
    #retorna a string na variavel frase2
    return frase2

frase = input("Digite uma frase para substituir os espaços por #: ")
#frase_decod recebe o valor retornado pela função subst
frase_decod = subst(frase)
print (frase_decod)