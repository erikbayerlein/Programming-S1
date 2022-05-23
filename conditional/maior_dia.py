# Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas pelo usuário. 
# Cada data deve ser composta por três valores inteiros, 
# em que o primeiro representa o dia, o segundo, o mês e o terceiro, o ano.

dia1 = int(input("Digite o primeiro dia: "))
if dia1 < 1 or dia1 > 30:
    print ("Entrada inválida.")
    exit()

mes1 = int(input("Digite o primeiro mês: "))
if mes1 < 1 or mes1 > 12:
    print ("Entrada inválida.")
    exit()

ano1 = int(input("Digite o primeiro ano: "))


dia2 = int(input("Digite o segundo dia: "))
if dia2 < 1 or dia2 > 30:
    print ("Entrada inválida.")
    exit()

mes2 = int(input("Digite o segundo mês: "))
if mes2 < 1 or mes2 > 12:
    print ("Entrada inválida.")
    exit()

ano2 = int(input("Digite o segundo ano: "))

if ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
    print ("As datas são iguais.")

elif ano1 > ano2:
    print ("A maior data é: %i / %i / %i" %(dia1, mes1, ano1))

elif ano2 > ano1:
    print ("A maior data é: %i / %i / %i" %(dia2, mes2, ano2))

elif ano1 == ano2 and mes1 > mes2:
    print ("A maior data é: %i / %i / %i" %(dia1, mes1, ano1))

elif ano1 == ano2 and mes2 > mes1:
    print ("A maior data é: %i / %i / %i" %(dia2, mes2, ano2))

elif ano1 == ano2 and mes1 == mes2:
    if dia1 > dia2:
        print ("A maior data é: %i / %i / %i" %(dia1, mes1, ano1))
    elif dia2 > dia1:
        print ("A maior data é: %i / %i / %i" %(dia2, mes2, ano2))

