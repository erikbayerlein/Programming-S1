frase = "O sabiá não sabia que o sábio sabia que o sabiá não sabia assobiar"

#a quantidade de ocorrência de
print (frase.count("sabiá"))
print (frase.count("sabia"))
print (frase.count("sábio"))
print (frase.count("s"))
print (frase.count("p"))

#posição da primeira ocorrência
print (frase.find("sabia"))
print (frase.find("sabia", 13))
print (frase.find("sabia", 13, 30))
print (frase.find("sabia", 13, 35))
#rfind para olhar da direita para a esquerda
print (frase.rfind("sabia"))
print (frase.rfind("sabia", 13))
print (frase.rfind("sabia", 13, 30))
print (frase.rfind("sabia", 13, 35))

#retorna uma lista de palavras na string usando sep como a string delimitadora
pa = "Ciencia da comp"
print (pa.split())

#substitui um caracter
frase2 = "segunda, terça, quarta"
print (frase2.replace("quarta", "sexta"))