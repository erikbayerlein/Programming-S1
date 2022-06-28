# Alice tem um aquário com vários peixes de espécies diferentes
#  . Para determinadas espécies existem mais de um peixe.
#  Como no aquário, existem muitos peixes,
#  ela guarda uma lista com todos os peixes. Escreva um programa que:
# a) Mostre a quantidade de espécies diferentes de peixes que existe no aquário de Alice.
# b) Identificar e tratar casos inválidos para o problema.
# Para casos inválidos, informar a saída: ‘entrada invalida’.
# Obs. Pode utilizar os métodos de listas ou strings.

# Exemplo: 
# Entrada: 5
# A B A B A 
# Saída 2

def num_especies(esp, num):
    num_esp = [esp[0]]
    for i in range(num):
        if esp[i] not in num_esp:
            num_esp.append(esp[i])
        else: 
            continue
    num2 = len(num_esp)
    return num2, num_esp

esp = []

while True:
    num = int(input("Digite o número de peixes que possui: "))
    if num <= 0:
        print ("Entrada inválida.")
    else:
        break

for i in range (num):
    esp.append(input("Digite a letra da espécie do peixe %i: " %(i+1)))

num_esp, esp_pres = num_especies(esp, num)

print ("A quantiade de peixes é: %i" %num)
print ("As espécies de cada peixe são: ", *esp)
print ("As espécies presentes no aquário são: ", *esp_pres)
print ("A quantidade de espécies diferentes são: %i" %num_esp)