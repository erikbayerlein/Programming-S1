# Correção de palavras. Em Português não existem palavras
# que iniciam com ‘ss’ ou ‘ç’. Faça um programa que solicite
# uma palavra e caso ela tenha ‘ss’ no início troque por ‘s’ ou se tiver ‘ç’ troque por ‘s’.
# Exemplo:
# ssardinha -> sardinha  çacola -> sacola

a = input("Digite uma palavra: ")

#transforma a em lista para ser alterada
list_a = list(a)
#transforma a em upper case para facilitar a verificação
maiusc = a.upper()

#verificação com ç
if maiusc[0] == "Ç":
    #primeiro lugar da lista de a recebe o S
    list_a[0] = "S"
    #list_a é transformado em string
    new_a = "".join(list_a)
    print (new_a)

#verificação com ss
elif maiusc[0] == "S" and maiusc[1] == "S":
    #remove o segunddo S da palavra
    list_a.pop(1)
    #tranforma a list_a em string
    new_a = "".join(list_a)
    print (new_a)

#caso esteja tudo correto
else:
    #transforma a list_a em string
    new_a = "".join(list_a)
    print ("Sua palavra está correta: %s" %(new_a))