import math

n1 = int(input("Digite um número entre 0 e 1000 para ser lido: "))

if n1 >= 1000 or n1 < 0:
    print ("Entrada inválida.")

else:
    # Quando n1 tiver apenas os algarismos das unidades
    if (n1 - 100) < 0 and (n1 - 10) < 0:
        print (n1,"=", n1,"unidades.")
    # Quando n1 tiver os algarismos das dezenas e das unidades
    elif (n1 - 100) < 0 and (n1 - 10) >= 0:
        dezena = n1 / 10
        unidade = n1 - (10 * math.floor (dezena))
        print (n1, "=", math.floor (dezena),"dezenas e", math.floor (unidade), "unidades.")
    # Quando n1 tiver os algarismos das centenas, das dezenas e das unidades
    else:
        centena = n1 / 100
        dezena = (n1 - (100 * math.floor (centena))) / 10
        unidade = n1 - (100 * math.floor (centena)) - (10 * math.floor (dezena))
        print (n1, "=", math.floor (centena),"centenas,", math.floor (dezena),"dezenas e", math.floor(unidade),"unidades.")
