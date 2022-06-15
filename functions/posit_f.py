#Escreva uma função em Python que recebe um número e verifica se ele é positivo

def pos(num):
    if num > 0:
        return "É positivo"
    elif num < 0:
        return "É negativo"
    else:
        return "É igual a 0"

x = int(input("Digite um número: "))
result = pos(x)
print (result)