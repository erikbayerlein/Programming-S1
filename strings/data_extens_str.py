#Data por extenso. Faça um programa que solicite a data de nascimento
#(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
# Data de Nascimento: 29/10/1973
# Saída: Você nasceu em 29 de Outubro de 1973.

#recebe as variaveis do dia, mes e ano
dia = input("Digite o dia em que você nasceu: ")
mes = int(input("Digite o mês em que você nasceu: "))
ano = input("Digite o ano em que você nasceu: ")

#criação de lista com todos os meses do ano e uma lista para armazenar o valoir do mes
list_mes = []
meses = ["Janeiro" , "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", \
    "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

print ("Data de Nascimento: %s/%i/%s" %(dia, mes, ano))

#colocar o mes dentro da lista criada
list_mes.append(mes)

#verificar e fazer a substituição do mês
for i in range(12):
    #quando o i for igual ao valor do mês - 1, fará a troca, 
    #pois a variavel mes pode ir de 1 a 12, mas a lista meses so possui 11 elementos
    if i == mes - 1:
        #retira o elemnto da lista
        list_mes.pop(0)
        #adciona o respectivo mês da lista meses
        list_mes.append(meses[i])
        #transforma a lista mes em string (new_mes)
        new_mes = "".join(list_mes)

print ("Você nasceus em %s de %s de %s" %(dia, new_mes, ano))