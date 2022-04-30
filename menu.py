# Escolher qual expressão matematica fazer \
# a partir de dois números

import math

opcao = int(input("Digite 1, se você que somar dois números. \
    Digite 2 se você quer dividir dois números. \
    Digite 3 se você quer a raíz quadrada de dois números: "))

if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    s = num1 + num2
    print ("A soma dos números é: %.2f" %(s))

elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print ("Entrada inválida.")
    else:
        d = num1 / num2
        print ("A divisão dos dois números é: %.2f" %(d))

elif opcao == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num1 >= 0 and num2 >= 0:
        raiz1 = math.sqrt(num1)
        raiz2 = math.sqrt(num2)
        print ("A raíz do primeiro número é: %.3f" %(raiz1))
        print ("A raíz do segundo número é: %.3f" %(raiz2))
    else:
        print ("Entrada inválida.")
