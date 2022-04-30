# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#  A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#  A mensagem "Reprovado", se a média for menor do que sete;
#  A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

m = (nota1 + nota2) / 2

if (nota1 > 10 or nota1 < 0) or (nota2 > 10 or nota2 < 0):
    print ("Suas notas não estão corretas.")

elif (nota1 <= 10 and nota1 >= 0) or (nota2 <= 10 and nota2 >= 0):
    if m == 10:
        print ("Aprovado com distinção.")
    elif m >= 7 and m < 10:
        print ("Aprovado com média ", m,".")
    else:
        print ("Reprovado com média ", m,".")