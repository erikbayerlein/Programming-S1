# Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#  Álcool:
#  até 20 litros, desconto de 3% por litro
#  acima de 20 litros, desconto de 5% por litro 
#  Gasolina:
#  até 20 litros, desconto de 4% por litro
#  acima de 20 litros, desconto de 6% por litro
#  Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
# o preço do litro do álcool é R$ 1,90.

preferencia = float(input("Digite 0 para escolher álcool ou digite 1 para escolher gasolina: "))

if preferencia == 1:
    print ("O preço da gasolina está R$ 2.50 por litro.")
    print ("Você ganhará descontos de 3% até 20 Litros ou 5% acima de 20 Litros.")
    quant_g = float(input("Quantos litros de gasolina você vai querer? "))
    if quant_g <= 20 and quant_g > 0:
        preco_g = ((2.5 * quant_g) * 97) / 100
        print ("Você precisará pagar: R$", preco_g)
    else:
        preco_g = ((2.5 * quant_g) * 95) / 100
        print ("Você precisará pagar: R$", preco_g)

elif preferencia == 0:
    print ("O preço do álcool está R$ 1.90 por litro.")
    print ("Você ganhará descontos de 4% até 20 Litros ou 6% acima de 20 Litros.")
    quant_a = float(input("Quantos litros de álcool você vai querer? "))
    if quant_a <= 20 and quant_a > 0:
        preco_a = ((1.9 * quant_a) * 94) / 100
        print ("Você precisará pagar: R$", preco_a)
    else:
        preco_a = ((1.9 * quant_a) * 94) / 100
        print ("Você precisará pagar: R$", preco_a)