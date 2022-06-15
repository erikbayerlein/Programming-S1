#  Resolva o problema anterior agora para que o seu programa
# leia um número de celular, e corrija o número no caso deste
# conter somente 8 dígitos, acrescentando o ‘9' na frente.
#  Obs1. Nesse problema considere também que o usuário além
# de poder informar o número com ou sem o traço separador;
# ele também pode informar com ou sem espaço.

while True:
    num = input("Digite o seu número de telefone sem DDD:")
    if len(num) >= 8 and len(num) <= 10:
        break
    print ("Entrada inválida.")

tam_num = len(num) - num.count("-") - num.count(" ")

if tam_num == 9 and num.count("-") == 1 or num.count(" ") == 1:
    list_num = list(num)
    list_num.insert(0, 9)
    print ("Está faltando o 9 na frente do número.")
    new_num = "".join(list_num)
    print ("O seu número corrigido é: %s" %new_num)

elif tam_num == 9 and num.count("-") == 0 and num.count(" ") == 0:
    print ("O seu número está correto: %s" %num)

elif tam_num == 8 and num.count("-") == 0 and num.count(" ") == 0:
    list_num = list(num)
    list_num.insert(0, 9)
    print ("Está faltando o 9 na frente do número.")
    new_num = "".join(list_num)
    print ("O seu número corrigido é: %s" %new_num)


