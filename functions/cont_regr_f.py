# Defina uma função contagem_regressiva que recebe
#  como parâmetro um inteiro representando o início da contagem.
#  Sua função deve contar (mostrando na tela) de n até o zero.

def cont_regr(num):
    while True:
        print (num)
        num = num - 1
        if num < 0:
            break

x = int(input("Digite um número para iniciar a contagem: "))
cont_regr(x)