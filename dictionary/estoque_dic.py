def criar_produto(k):
    estoque = []
    for i in range(k):
        produto = {}
        produto["Código"] = int(input("Digite o código do produto: "))
        produto["Preço"] = float(input("Digite o preço do produto: "))
        produto["Quantidade"] = int(input("Digite o quantidade do produto: "))
        estoque.append(produto)
    return estoque


def mostrar_produto(estoque, k):
    total_preco = 0
    total_qntd = 0
    
    for chave in estoque:
        total_preco += (chave["Preço"] * chave["Quantidade"])
    print(f"O valor total do estoque é R${total_preco}")

    for chave in estoque:
        total_qntd += chave["Quantidade"]
    print(f"A quantidade total de peças é: {total_qntd}")

    
def buscar(estoque):
    codigo = int(input("Digite o código do produto para a busca: "))
    registro = {}
    for estoque in estoque:
        if estoque["Código"] == codigo:
            print("oi")


while True:
    k = int(input("Digite a quantidade de produtos para adicionar no estoque: "))
    if k > 0 and k <= 10:
        break
    else:
        print("Entrada inválida.")

estoque = criar_produto(k)

mostrar_produto(estoque, k)

buscar(estoque)