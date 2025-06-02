# Retorna o valor apenas se for numérico
def get_value(msg):
	while True:
		value = input(msg)
		try:
			return float(value)
		except ValueError:
			print(f"'{value}' não é um valor numérico válido.")

# Retorna 'True' se todas as notas forem maiores que '7'
def is_passed(mat1, mat2, mat3):
	return mat1 > 7 and mat2 > 7 and mat3 > 7

# Armazena os valores das notas
mat1 = get_value("Insira a nota da matéria 1: ")
mat2 = get_value("Insira a nota da matéria 2: ")
mat3 = get_value("Insira a nota da matéria 3: ")

# Verifica se o aluno passou e mostra na tela
if (is_passed(mat1, mat2, mat3)):
	print("Aluno aprovado!")
else:
	print("Aluno reprovado.")