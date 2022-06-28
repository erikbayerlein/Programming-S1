# Faça uma função que recebe uma frase e retorna o número
# de palavras que a frase contém. Considere que a palavra
# pode começar e/ou terminar por espaços. 
# A entrada e saída de dados devem ser feitas no programa principal.

def num_palavras (frase):
    list_frase = list(frase.lower())
    cont = 0
    if list_frase[0] == " ":
        list_frase.pop(0)
    if list_frase[-1] == " ":
        list_frase.pop(-1)
    for i in range(len(list_frase)):
        if list_frase[i] == " ":
            cont += 1
        else: continue
    cont_r = cont + 1
    return cont_r
    
frase = input("Digite uma frase: ")
num = num_palavras(frase)
print ("O número de palavras da frase é: %i" %num)