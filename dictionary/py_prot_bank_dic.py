def menu_principal():

    opcoes = ["1. Inserir sequência","2. Consultar sequência por nome", "3. Listar sequências por organismo",\
        "4. Listar todas as sequências", "5. Finalizar"]

    print("******* PyProtBank *******")
    for i in range(5):
        print(opcoes[i])


    while True:
        opt = int(input("Digite a opção desejada: "))
        if opt >= 1 and opt <= 5:
            break
        else:
            print("Entrada inválida.")

    if opt == 1:
        sequencias = []
        sequencias.append(opcao1())

'''   elif opt == 2:
        opcao2()

    elif opt == 3:
        opcao3()'''

    elif opt == 4:
        opcao4(sequencias)

'''    elif opt == 5:
        exit()'''


def opcao1():
    sequencia = {}
    sequencia["Nome"] = input("Diigite o nome da sequência: ")
    sequencia["Descrição"] = input("Digite a descrição: ")
    sequencia["Organismo"] = input("Digite o nome do organismo: ")
    sequencia["Número de átomos"] = int(input("Digite o número de átomos: "))

    print("Nome:", sequencia["Nome"])
    print("Descrição:", sequencia["Descrição"])
    print("Organismo:", sequencia["Organismo"])
    print("Número de átomos:", sequencia["Número de átomos"])

    return sequencia


def opcao4(sequencias):


menu_principal()
