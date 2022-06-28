# Alice tem um aquário com vários peixes de espécies diferentes
#  . Para determinadas espécies existem mais de um peixe.
#  Como no aquário, existem muitos peixes,
#  ela guarda uma lista com todos os peixes. Escreva um programa que:
# a) Mostre a quantidade de espécies diferentes de peixes que existe no aquário de Alice.
# b) Identificar e tratar casos inválidos para o problema.
# Para casos inválidos, informar a saída: ‘entrada invalida’.
# Obs. Pode utilizar os métodos de listas ou strings.

# Exemplo: Entrada: 5
# A B A B A 
# Saída 2



import string

alfabeto = list(string.ascii_lowercase())

while True:
    num = int(input("Digite o número de peixes que possui: "))
    if num <= 0:
        print ("Entrada inválida.")
    else:
        break

