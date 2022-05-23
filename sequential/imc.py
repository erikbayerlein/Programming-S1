print ("Vamos calcular o seu IMC.")

altura = float(input("Digite a sua altura."))
peso = float(input("Digite o seu peso."))

imc = peso/(altura*altura)

print ("O seu IMC é: ", round (imc, 2),".")