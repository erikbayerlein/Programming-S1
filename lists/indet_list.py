# Faça um programa que leia um número indeterminado de valores,
#  correspondentes a notas, encerrando a entrada de dados
#  quando for informado um valor igual a -1 (que não deve ser armazenado).
#  Após esta entrada de dados, faça:

#a) Mostre a quantidade de valores que foram lidos;
#b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#d) Calcule e mostre a soma dos valores;
#e) Calcule e mostre a média dos valores;
#f) Calcule e mostre a quantidade de valores acima da média calculada;

A = []
B = []
soma = 0

while True:
    n = int(input("Digite um número: "))
    if n == -1:
        break
    else:
        A.append(n)

print (len(A))

print (A)

copia_A = A.copy()
copia_A.reverse()

for i in range (len(copia_A)):
    print (copia_A[i])

for i in range(len(A)):
    soma += A[i]

print (soma)

media = soma / len(A)

print (media)

for i in range (len(A)):
    if A[i] > media:
        B.append(A[i])

print ("Os valores acima da média são: " , B)