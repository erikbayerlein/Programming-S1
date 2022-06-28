# Faça uma função que recebe uma string que representa
# uma cadeia de DNA e gera a cadeia complementar. 
# A entrada e saída de dados devem ser feitas pelo programa principal.
#Entrada: AATCTGCAC 
#Saída: TTAGACGTG

def dna_complemento (dna_origem):
    list_dna = list(dna_origem)
    dna_2 = []
    for i in range(len(list_dna)):
        if list_dna[i] == "A":
            dna_2.append("T")
        elif list_dna[i] == "T":
            dna_2.append("A")
        elif list_dna[i] == "C":
            dna_2.append("G")
        elif list_dna[i] == "G":
            dna_2.append("C")
    dna = "".join(dna_2)
    return dna

letras = ["A", "C", "T", "G"]

#while True:
dna_origem = input("Digite a sequência inicial de DNA: ")
    #if letras in dna_origem.upper():
        #break
    #else:
        #print ("Entrada inválida. Tente novamente.")
print (dna_origem)

dna_comp = dna_complemento(dna_origem)
print (dna_comp)