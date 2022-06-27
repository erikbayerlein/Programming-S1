# Faça uma função que recebe uma string que representa
# uma cadeia de DNA e gera a cadeia complementar. 
# A entrada e saída de dados devem ser feitas pelo programa principal.
#Entrada: AATCTGCAC 
#Saída: TTAGACGTG

import random

mat = []

for i in range (10):
    linha = []
    for j in range (10):
        linha.append(0)
    mat.append(linha)

print (mat)

k = 0

while k < 10:
    while True:    
        i = random.choice(range(10))
        j = random.choice(range(10))
        if mat[i][j] == 1:
            break
        else:
            mat[i][j] = 1
            k += 1
            break
        
print (mat)