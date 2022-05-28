#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
#pelo atleta em seus saltos e depois informe o nome,
#os saltos e a média dos saltos. O programa deve ser encerrado
#quando não for informado o nome do atleta.
#A saída do programa deve ser conforme o exemplo abaixo:

#Atleta: Rodrigo Curvêllo
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

n = input("Digie o nome do atleta: ")

soma = 0

if n == "":
    print ("Programa encerrado pois não foi digitado o nome.")
    exit()

D = [0]*5

for i in range (5):
    altura = float(input("Digite a altura do %iº do(a) %s: " %(i+1, n)))
    D[i] = altura

for i in range (5):
    soma += D[i]

media = soma / 5

print ("Resultado final: ")
print ("Atleta: %s" %(n))
print ("Saltos: ", D)
print ("Média dos saltos: %.1fm" %(media))