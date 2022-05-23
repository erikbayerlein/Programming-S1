# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite o tamanho de um arquivo para download em MB: "))
velocidade = float(input("Digite a velocidade da sua internet em Mbps: "))

tempo = (tamanho / velocidade) / 60

print ("O tempo aproximado de donwload do arquivo em minutos é: ", round (tempo,3))