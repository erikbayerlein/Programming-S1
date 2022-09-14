#Lista que conterá os dicionários
contatos = []
#for para preenchimento dos contatos de acordo com a quantidade
for i in range(5):
    #dicionario que conterá as informacoes
    contato = {}
    #entrada de dados
    contato["Nome"] = input("Digite o seu nome: ")
    contato["Endereço"] = input("Digite o seu endereço: ")
    contato["Número"] = int(input("Digite o seu número: "))
    #dicionario é adicionado à lista
    contatos.append(contato)

#print da lista com os dicionarios preenchidos
print(contatos)