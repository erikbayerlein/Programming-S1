print ("Vamos calcular diferentes áreas.")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

triang = (a*c) / 2

print ("A área do triangulo retangulo de base A e altura C é: ", triang,".")

circ = 2 * 3.14159 * c

print ("A área do círculo de raio C é: ", round (circ, 2),".")

trap = ((a+b) * c) / 2

print ("A área do trapézio de bases A e B e altura C é: ", trap,".")

quad = b*b

print ("A área do quadrado de lado B é: ", quad,".")

ret = b*a

print ("A área do retângulo de lados A e B é: ", ret,".")