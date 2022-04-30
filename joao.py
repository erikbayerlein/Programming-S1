#Calcular a quantidade de litros gastos em uma viagem
# dando o tempo e a velocidade

tempo = int(input("Quanto tempo gasto na viagem?"))
v = int(input("Qual foi a velocidade média?"))

# 12km/L
distancia = tempo * v
litros = distancia / 12

litros_gasto = round(litros, 3)

print ("A quantidade de litros necessária é: %.3f" %(litros_gasto))