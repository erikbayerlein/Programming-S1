#  Para cada resposta afirmativa (isto é, sim) o produto ganha uma estrela;
#  Produtos fora do prazo de validade recebem automaticamente 0 estrelas e não passam no teste;
#  Produtos com 3 ou menos estrelas não passaram no teste.
# A carne está com gordura branca e firme?
# A carne possui cor vermelho-brilhante?
# A carne está em uma temperatura inferior a 7 graus? A carne possui cheiro agradável?
# A carne ainda está dentro do prazo de validade?

print ("Digite 1 para sim e 0 para não")

p1 = int(input("A carne está com gordura branca e firme?"))
p2 = int(input("A carne possui cor vermelho-brilhante?"))
p3 = int(input("A carne está em uma temperatura inferior a 7 graus?"))
p4 = int(input("A carne possui cheiro agradável?"))
p5 = int(input("A carne ainda está dentro do prazo de validade?"))

s = p1+p2+p3+p4+p5

if p5 == 0:
    print ("A carne não passou no teste, pois está fora da validade.")

elif s <= 3:
    print ("A carne não passou no teste.")
elif s > 3 and s <=5:
    print ("A carne passou no teste.")