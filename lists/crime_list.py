# Utilizando listas refaça o programa que faz 5 perguntas
# para uma pessoa sobre um crime. As perguntas são:
#  "Telefonou para a vítima?" 
#  "Esteve no local do crime?" 
#  "Mora perto da vítima?"
#  "Devia para a vítima?"
#  "Já trabalhou com a vítima?"
#  O programa deve no final emitir uma classificação sobre a participação da pessoa
# no crime. Se a pessoa responder positivamente
#  a 2 questões ela deve ser classificada como "Suspeita",
#  entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#  Caso contrário, ele será classificado como "Inocente".

P = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ",\
     "Devia para a vítima? ", "Já trabalhou com a vítima? "]
count = 0

for i in range (5):
    r = input(P[i])
    if r == "sim":
        count += 1

if count == 5:
    print ("Assassino. (%i pontos)" %count)
elif count >= 3 and count <= 4:
    print ("Cúmplice. (%i pontos)" %count)
elif count == 2:
    print ("Supeita. (%i pontos)" %count)
else:
    print ("inocente. (%i pontos)" %count)