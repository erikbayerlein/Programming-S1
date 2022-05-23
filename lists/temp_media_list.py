#  Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#  Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, etc.).

M = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",\
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
T = [0]*12
Z = []

x = 0

for i in range (12):
    T[i] = float(input("Digite a temperatura média de %s: " %M[i]))
    x += T[i]

media = x/12
print (round (media, 2))

for i in range (12):
    if T[i] > media:
        Z.append(T[i])

for i in range (len(Z)):
    print ("%s: %.2f (temperatura acima da média)" %(M[i], Z[i]))
