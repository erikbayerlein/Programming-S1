# Faça um programa que leia 2 strings e informe
# o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem
# o mesmo comprimento e são iguais ou diferentes no conteúdo.

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

print ("O conteúdo da primeira string é: %s. Ela possui %i caracteres." %(str1, len(str1)))
print ("O conteúdo da segunda string é: %s. Ela possui %i caracteres." %(str2, len(str2)))

if len(str1) == len(str2):
    print ("As strings possuem o mesmo comprimento.")
else:
    print ("As strings não possuem o mesmo comprimento.")

if str1 == str2:
    print ("As strings são iguais.")
else:
    print ("As strings são diferentes.")