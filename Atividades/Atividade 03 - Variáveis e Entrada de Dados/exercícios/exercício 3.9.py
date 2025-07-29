# Retorna o valor apenas se for inteiro
def get_value(msg):
	while True:
		value = input(msg)
		if value.isnumeric():
			return int(value)
		print(f"'{ value }' não é um valor inteiro.")

# Retorna a conersão dos valores para segundos
def get_seconds(days, hours, minutes, seconds):
	total  = days * 24 * 60 * 60
	total += hours * 60 * 60
	total += minutes * 60
	total += seconds

	return total

# Armazena os valores de dia, hora, minuto e segundo
days = get_value("Insira um valor em dias[d]: ")
hours = get_value("Insira um valor em horas[h]: ")
minutes = get_value("Insira um valor em minutos[m]: ")
seconds = get_value("Insira um valor em segundos[s]: ")

# Mostra o total de tempo em segundos
print(f"[{ days } dias], "
	  f"[{ hours } horas], "
	  f"[{ minutes } minutos], "
	  f"[{ seconds } segundos] "
	  f"-> { get_seconds(days, hours, minutes, seconds) } segundo(s).")
