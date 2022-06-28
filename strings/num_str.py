# Valida e corrige número de telefone.
# Faça um programa que leia um número de telefone,
# e corrija o número no caso deste conter somente 7 dígitos,
# acrescentando o '3' na frente.


num = input("Digite o seu número de telefone: ")
list_num = list(num)

if "-" in list_num:
    list_num.remove("-")
elif " " in list_num:
    list_num.remove(" ")

if len(list_num) == 7:
    list_num.insert(0, "3")
    list_num.insert(4, "-")
    num_correto = "".join(list_num)
    print("Seu número possui apenas 7 dígitos")
    print("O correto é: %s" %num_correto)
else:
    list_num.insert(4, "-")
    num_correto = "".join(list_num)
    print("Seu número está correto: %s" %num_correto)