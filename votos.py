quant_eleitores = int(input("Digite a quantidade de eleitores: "))

if quant_eleitores <= 0:
    print ("Entrada inválida")
    exit()

count_votos1 = 0
count_votos2 = 0
count_votos3 = 0

for i in range (1, quant_eleitores):
    voto = int(input("Digite o voto do eleitor %i: " %(i)))
    if voto == 1:
        count_votos1 += 1
    elif  voto == 2:
        count_votos2 += 1
    elif voto == 3:
        count_votos3 += 1
    else:
        print ("Entrada inválida")
        exit()

print ("%i voto(s) para o candidato 1.\
    \n%i voto(s) para o candidato 2.\
    \n%i voto(s) para o candidato 3." %(count_votos1, count_votos2, count_votos3))