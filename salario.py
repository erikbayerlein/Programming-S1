print ('Responda as seguintes respostas com 1 para sim e 0 para nao')

p1 = int(input('Telefonou para a vítima?'))
p2 = int(input('Esteve no local do críme?'))
p3 = int(input('Mora perto da vítima?'))
p4 = int(input('Devia para a vítima?'))
p5 = int(input('Já trabalhou com a vítima?'))

soma = p1+p2+p3+p4+p5

if soma == 0:
    print ('Você está livre')

if soma > 5:
    print ('Entrada inválida')

if soma == 5:
    print ('Você é o assassino')
elif soma == 3 or soma == 4:
    print ('Você é cúmplice')
elif soma == 2:
    print ('Você é suspeita')
