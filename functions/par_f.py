#Escreva uma função em Python que recebe um número e verifica se ele é um número par

def par(num):
    if num % 2 == 0:
        return "É par"
    else:
        return "Não é par"

x = int(input("Digite um número: "))
result = par(x)
print (result)