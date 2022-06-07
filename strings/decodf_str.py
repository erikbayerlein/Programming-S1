# Faça um programa que peça para o usuário entrar com uma string,
#  depois mostre a string codificada, trocando
# a letra a por um 4,
# a letra o por um *
# a letra s por 5.
# Aceite caracteres maiúsculos e minúsculos e não utilize os métodos
#de strings replace ou translate.
# Exemplo:
# Entrada: Nada como um dia depois do outro.
# Saída: N4d4 c*m* um di4 dep*i5 d* *utr*.

c = 0
k = 0
z = 0

#entrada valida com a, o ou s
while True:
    frase = input("Digite uma frase: ")
    if "a" in frase.lower() or "o" in frase.lower() or "s" in frase.lower():
        break
    print ("Entrada inválida. Sua frase não possui a's , s's ou o's.")

#transforma a frase minuscula em lista
list_frase = list(frase.lower())

#verifica os elemtnos da lista para achar um a
for i in list_frase:
    if i == "a":
        #retira o elemento da lista em q possui um a
        list_frase.pop(c)
        #insere um novo elemento no lugar
        list_frase.insert(c, "4")
    #contador para a substituição dos elementos
    c += 1

for i in list_frase:
    if i == "o":
        list_frase.pop(k)
        list_frase.insert(k, "*")
    k += 1

for i in list_frase:
    if i == "s":
        list_frase.pop(z)
        list_frase.insert(z, "5")
    z += 1

#tranforma a lista em string
new_frase = "".join(list_frase)

#print da string modificada
print (new_frase)