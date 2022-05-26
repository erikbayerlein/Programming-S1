# Com base na lista = [1, 10, 2, 8, 9, 2, 5], 
# aplique as operações abaixo para a cópia da lista 
# e informe o seu retorno para o seguintes itens:
# a) Adiciona o elemento 10 ao final da lista lista
# b) Adiciona o elemento 6 na posição 2 da lista lista
# c) Remove o primeiro elemento 2 da lista
# d) Remove o último elemento da lista
# e) Remove o último elemento da lista e o retorna
# f) Insere o elemento 4 na posição 2
# g) Ordene a lista em ordem decrescente
# h) Imprime a lista original e sua cópia

from string import printable
from traceback import print_tb


lista = [1, 10, 2, 8, 9, 2, 5]
copia = lista.copy()

#a
copia.append(10)
#b
copia.insert(2, 6)
#c
copia.remove(2)
#d
copia.pop()
#e
el = copia.pop()
print (el)
#f
copia.insert(2, 4)
#g
copia.sort()
#h
print (lista)
print (copia)
