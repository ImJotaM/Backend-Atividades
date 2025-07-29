# Retorna o valor apenas se for numérico
def get_value(msg):
	while True:
		value = input(msg)
		try:
			return float(value)
		except ValueError:
			print(f"'{value}' não é um valor numérico válido.")

# Armazena o valor do salário e da porcentagem de aumento
salary = get_value("Insira o salário que irá receber aumento (R$): ")
porcentage = get_value("Insira a porcentagem de aumento do salário (%): ")

# Mostra o novo salário
print(f"O novo salário após o aumento de {porcentage}% é: {salary + salary * (porcentage / 100)}")