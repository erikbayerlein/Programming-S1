# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#  comprar apenas latas de 18 litros;
#  comprar apenas galões de 3,6 litros;
#  misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

m2 = float(input('Quantos metros quadrados você gostaria de pintar?'))

# 1L -> 6m2
# Latas de 18L custam 80
# Galoes de 3.6L custam 25

litros_nec = m2 * 6.00
latas = litros_nec * 80.00
galoes = litros_nec * 25.00

print ("Você precisará de ", litros_nec,"litros de tinta.")
print ("Três situações para a compra da tinra são possíveis: ")
print ("Se comprar latas de 18L, as quais custam R$ 80.00, você pagará: ", latas,".")
print ("Se comprar galões de 3.6L, os quais custam R$ 25.00, você pagará: ", galoes,".")
