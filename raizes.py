# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#  Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o 
# programa não deve fazer pedir os demais valores, sendo encerrado;
#  Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#  Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#  Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print ("Vamos calcular as raízes de uma equação do segundo grau (ax2 + bx + c = 0.")

a = float(input("Insira o valor de a: "))

if a == 0:
    print ("A equação não é do segundo grau, pois a = 0.")

else:
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))

    delta = (b**2) - 4*a*c
    raiz = math.sqrt (delta)
    x1 = (-b + raiz) / 2*a
    x2 = (-b - raiz) / 2*a

    if delta < 0:
        print ("A equação não possui valores reais.")
    elif delta == 0:
        print ("A equação possui apenas um valor real: ", x1)
    else:
        print ("A equação possui dois valores reais: ", round(x1,2), round(x2,2))
