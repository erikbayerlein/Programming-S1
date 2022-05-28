# Faça um programa que recebe duas listas com dados de entradas fornecidos pelo usuário
#  e cria uma terceira lista que deve receber, primeiramente, 
# todos os números ímpares da primeira e, depois, receber todos
#  os números pares da segunda lista. Seu algoritmo deve retornar
#  a lista resultante e a soma dos números desta lista.
#Entrada:
#lista-um = [1,4,27,5] lista-dois = [7,-9,2,6,5,10]
#Saída:
#lista-resultante = [1, 27, 5, 2, 6,10] 51


#primeira lista para os numeros pares
eu_amo_minha_namorada = [] 

#segunda lista para os numeros impares
minha_namorada_eh_linda = []

#lista que sera preenchida
mo = []

#soma dos elementos preenchidos da lista mo
kfc = 0

print ("Digite 0 para parar de preencher as listas.")

# preenchimento da primeira lista
while True:
    n1 = int(input("Digite um número para a primeira lista: "))
    if n1 == 0:
        break
    eu_amo_minha_namorada.append(n1)

#preenchimento da segunda lista
while True:
    n2 = int(input("Digite um número para a segunda lista: "))
    if n2 == 0:
        break
    minha_namorada_eh_linda.append(n2)

print (eu_amo_minha_namorada)
print (minha_namorada_eh_linda)

#preenchimento da terceira lista com os impares da primeira lista
for i in range (len(eu_amo_minha_namorada)):
    if eu_amo_minha_namorada[i] % 2 != 0:
        mo.append(eu_amo_minha_namorada[i])

#preenchimento da terceira lista com os pares da segunda lista
for i in range (len(minha_namorada_eh_linda)):
    if minha_namorada_eh_linda[i] % 2 == 0:
        mo.append(minha_namorada_eh_linda[i])

#soma da terceira lista
for i in range (len(mo)):
    kfc += mo[i]

print (mo)
print (kfc)