import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale 'pt_BR.UTF-8' não suportado. Usando o padrão do sistema.")
    locale.setlocale(locale.LC_ALL, '')

itens_venda = [
    ("Produto A Longo Nome", 150.75),
    ("Item B", 25.00),
    ("C-123", 12345.80),
    ("Dígito Simples", 5.99)
]

LARGURA_ITEM = 25
LARGURA_PRECO = 10
LARGURA_TOTAL = LARGURA_ITEM + LARGURA_PRECO + 1

print(f"{'Item':<{LARGURA_ITEM}} {'Preço':>{LARGURA_PRECO}}")
print('-' * LARGURA_TOTAL)

for item, preco in itens_venda:
    preco_formatado = locale.format_string('%.2f', preco, grouping=True)
    print(f"{item:<{LARGURA_ITEM}} {preco_formatado:>{LARGURA_PRECO}}")
