# Retorna o valor apenas se for numérico
def get_value(msg):
	while True:
		value = input(msg)
		try:
			return float(value)
		except ValueError:
			print(f"'{value}' não é um valor numérico válido.")

# Armazena o valor em metro
meter = get_value("Insira um valor em metros(m): ")

print()

# Mostra o valor em metros(m) convertido em milímetros(mm).
print(f"Conversão [m] para [mm]:")
print(f"{ meter } m -> { meter * 1000 } mm")