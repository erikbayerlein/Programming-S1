# Dado um número recebido pelo usuário (n > 0), 
# calcule a soma de números pares até este número (incluindo ele mesmo).

# Dados de entrada (até que número deseja ser somado)
num = int(input())

# Contador para os números pares
count_par = 0

# Caso o usuário digite números negativos ou 0
while num <= 0:
    num = int(input())
    
# Somar todos os i's pares até o número escolhido
for i in range (1,num + 1):
    if i % 2 == 0:
        count_par += i

# Dado de saída (soma final de todos os números pares)
print (count_par)
