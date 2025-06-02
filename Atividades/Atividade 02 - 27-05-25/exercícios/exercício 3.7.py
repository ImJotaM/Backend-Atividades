# Retorna o valor apenas se for inteiro
def get_value(msg):
	while True:
		value = input(msg)
		if value.isnumeric():
			return int(value)
		print(f"'{ value }' não é um valor inteiro.")

# Armazena os valores solicitados
num1 = get_value("Insira um número inteiro: ")
num2 = get_value("Insira outro número inteiro: ")

# Mostra a soma dos dois valores na tela
print(f"A soma dos dois números fornecidos é { num1 + num2 }.")