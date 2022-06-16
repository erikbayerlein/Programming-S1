#  Faça um programa que percorre duas listas e intercala os elementos de ambas,
# formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor.
#  Exemplo:
#  lista1 = [1, 2, 3, 4]
#  lista2 = [10, 20, 30, 40, 50, 60]
#  lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]
#  Obs. Defina funções, por exemplo, para preencher, 
# imprimir e percorrer a lista para intercalar os elementos das listas 1 e 2, etc.

#função para o preenchimento de listas
def preenc_list():
    lista = []
    print ("Para parar de preencher a lista, digite um número negativo.")
    while True:
        num = int(input("Digite um número para adicionar à lista: "))
        if num < 0:
            print ("Lista finalizada.")
            break
        lista.append(num)
    #retorna a lista preenchida
    return lista

#função para intercalar as listas
def intercal(x, y):
    #criação de uma nova lista para receber as listas intercaladas
    _lista_3 = []
    i = 0
    #if para verificar qual a menor lista começar devidamente pela menor
    if len(x) > len(y):
        x = lista2
        y = lista1
    #intercala a lista até o i ser igual ao tamanho da menor lista
    while i < len(x):
        #recebe primeiro o elemento da menor lista
        _lista_3.append(x[i])
        #em seguida, receber o elemento da maior lista
        _lista_3.append(y[i])
        #contador para mudar os elementos inseridos e verificar o tamanho
        i += 1
    #coloca os elementos da maior lista de onde parou a contagem do i até o final
    for k in range(i, len(y)):
        _lista_3.append(y[k])
    #retorna a lista intercalada
    return _lista_3

#chama a função para preencher a lista1
lista1 = preenc_list()
#chama a função para preencher a lista2
lista2 = preenc_list()
#chama a função para intercalar lista1 e lista2
lista3 = intercal(lista1, lista2)
print (lista1)
print (lista2)
print (lista3)