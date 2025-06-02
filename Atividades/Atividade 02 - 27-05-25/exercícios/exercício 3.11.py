# Retorna o valor apenas se for numérico
def get_value(msg):
	while True:
		value = input(msg)
		try:
			return float(value)
		except ValueError:
			print(f"'{value}' não é um valor numérico válido.")

# Armazena o preço da mercadoria e da porcentagem de desconto
price = get_value("Insira o preço da mercadoria (R$): ")
porcentage = get_value("Insira a porcentagem de desconto da mercadoria (%): ")

# Mostra o novo preço
print(f"O novo preço após o desconto de {porcentage}% é: {price - price * (porcentage / 100)}")