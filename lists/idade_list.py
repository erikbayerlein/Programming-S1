idade = [0]*5
altura = [0]*5

for i in range (5):
    idade[i] = int(input("Digite a idade da %iº pessoa: " %(i+1)))
    copia_i = idade.copy()

for i in range (5):
    altura[i] = float(input("Digite a altura da %iº pessoa: " %(i+1)))
    copia_a = altura.copy()

copia_a = altura.copy()
copia_i = idade.copy()

copia_a.reverse()
copia_i.reverse()

print (copia_a)
print (copia_i)