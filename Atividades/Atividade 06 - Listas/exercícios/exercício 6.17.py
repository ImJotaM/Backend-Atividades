estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

total = 0
print("Vendas:\n")

while True:
    produto_vendido = input("Digite o nome do produto (ou 'fim' para encerrar): ").lower()
    if produto_vendido == 'fim':
        break

    if produto_vendido in estoque:
        quantidade_vendida = int(input(f"Digite a quantidade de '{produto_vendido}' vendida: "))
        preco = estoque[produto_vendido][1]
        custo = preco * quantidade_vendida

        if quantidade_vendida <= estoque[produto_vendido][0]:
            print("%12s: %3d x %6.2f = %6.2f" % (produto_vendido, quantidade_vendida, preco, custo))
            estoque[produto_vendido][0] -= quantidade_vendida
            total += custo
        else:
            print(f"Estoque insuficiente de {produto_vendido}. Temos apenas {estoque[produto_vendido][0]} unidades.")
    else:
        print("Produto não encontrado no estoque.")

print("\nCusto total: %21.2f\n" % total)
print("Estoque atualizado:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])