# Faça A série de Fibonacci é formada pela sequência: 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# F(n+2)=F(n+1)+F(n)

n = int(input("Digite até que termo você gostaria de ver a Série de Fibonacci: "))

#while n <= 0:
    #n = int(input("Entrada inválida, digite outro número: "))

s = n + 2

f1 = 0
f2 = 1
f3 = f1 + f2
fn = 0

for i in range (1,n):
    fn = f1 + f2
    print (fn)
    fn += fn 
    print (fn)