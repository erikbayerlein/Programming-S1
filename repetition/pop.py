# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
 # e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
 # Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

A = 80000
B = 200000

time = 1

new_A = A * (103/100)
new_B = B * (101.5/100)

while new_A < new_B:
    new_A = new_A * (103/100)
    new_B = new_B * (101.5/100)
    time += 1

print ("A população de A será: %i" % (new_A))
print ("A população de B será: %i" % (new_B))
print ("Passarão %i anos para ultrapassar a população" %(time))