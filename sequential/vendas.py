# Faça um programa que leia o nome de um vendedor, 
# o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, 
# informar o total a receber no final do mês, com duas casas decimais.
#  Entrada
#  O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de com duas casas decimais, 
# representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.
#  Saída
#  Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

nome = input("Qual o seu nome? ")
sf = float(input("Digite o seu salário fixo: "))
vendas = float(input("Digite o total de vendas realizadas (em reais) por você no mês: "))

comissao = (15 / 100) * vendas
st = sf + comissao

print ("Você deverá receber R$ ", comissao,"de comissão.")
print ("O seu salário deverá ser R$ ", round(st,2),".")