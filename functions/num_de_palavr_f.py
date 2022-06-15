# Faça uma função que recebe uma frase e retorna o número
# de palavras que a frase contém. Considere que a palavra
# pode começar e/ou terminar por espaços. 
# A entrada e saída de dados devem ser feitas no programa principal.

def entrada():
    frase = input("Digite uma frase: ")
    return frase

def num_palavras(x):
    x_list = list(x)
    print (x_list)
    for i in range(len(x_list)):
        if x_list[i] == " " and x_list[1] != " " and x_list[-1] != " ":
            cont = 1
            cont += 1
        elif x_list[i] == " " and x_list[1] == " " and x_list[-1] != " ":
            cont = 0
            cont += 1
        elif x_list[i] == " " and x_list[1] != " " and x_list[-1] == " ":
            cont = 0
            cont += 1
        elif x_list[i] == " " and x_list[1] == " " and x_list[-1] == " ":
            cont = -1
            cont -= 1
    return cont

frase = entrada()
num = num_palavras(frase)
print("O número de palavras na frase é: %i" %num)