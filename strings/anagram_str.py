#Um anagrama é uma palavra que é feita a partir
#  da transposição das letras de outra palavra ou frase.
#  Por exemplo, “Iracema” é um anagrama para “America”.
#  Escreva um programa que decida se uma string é um anagrama
#  de outra string, ignorando os espaços em branco. 
# O programa deve considerar maiúsculas e minúsculas como
#  sendo caracteres iguais, ou seja, “a” = “A”.

a1 = input("Digite a primeira palavara: ")
a2 = input("Digite a segunda palavra: ")

a1_low = a1.lower()
a2_low = a2.lower()

if len(a2) == len(a1):
    for i in a1_low:
        for k in a2_low:
            if i == k:
                break

if len(a2) == len(a1):
    for i in range(len(a1_low)):
        a1_low.count(i)

else:
    print ("Não são anagramas, pois possuem tamanhos diferentes.")