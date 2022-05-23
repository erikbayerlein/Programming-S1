# João Papo-de-Pescador, 
# homem de bem, comprou um 
# microcomputador para controlar o 
# rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que 
# o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a 
# quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

kg = float(input('Olá João Papo-de-Pescador. Quantos Kg de peixe você trouxe hoje?'))

excesso = kg - 50

if excesso <= 0:
    print ('Você está dentro do regulamento. Não precisará pagar multa.')

else:
    multa = excesso * 4.00
    print ('Você terá que pagar R$ ', multa,' de multa, pois trouxe', excesso,'Kg em excesso')