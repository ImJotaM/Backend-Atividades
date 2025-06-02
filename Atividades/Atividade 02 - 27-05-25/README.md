# Atividade 01 - 22-04-25

## Exercícios

 - [Exercício 3.1](#exercício-31)
 - [Exercício 3.2](#exercício-32)
 - [Exercício 3.3](#exercício-33)
 - [Exercício 3.5](#exercício-35)
 - [Exercício 3.6](#exercício-36)
 - [Exercício 3.7](#exercício-37)
 - [Exercício 3.8](#exercício-38)
 - [Exercício 3.9](#exercício-39)
 - [Exercício 3.10](#exercício-310)
 - [Exercício 3.11](#exercício-311)

### Exercício 3.1

![alt text](../../imgs/Atividade%2002/image-1.png)

#### Resolução

| Número   | Tipo numérico                    |
|----------|----------------------------------|
| 5        | [X] inteiro [ ]  ponto flutuante |
| 5.0      | [ ] inteiro [X]  ponto flutuante |
| 4.3      | [ ] inteiro [X]  ponto flutuante |
| -2       | [X] inteiro [ ]  ponto flutuante |
| 100      | [X] inteiro [ ]  ponto flutuante |
| 1.333    | [ ] inteiro [X]  ponto flutuante |

### Exercício 3.2

![alt text](../../imgs/Atividade%2002/image-2.png)

#### Resolução

| Expressão | Resultado          |
|-----------|--------------------|
| a == c    | [ ] True [X] False |
| a < b     | [X] True [ ] False |
| d > b     | [ ] True [X] False |
| d == f    | [ ] True [X] False |
| a == b    | [ ] True [X] False |
| c < d     | [ ] True [X] False |
| b > a     | [X] True [ ] False |
| c >= f    | [X] True [ ] False |
| c <= c    | [X] True [ ] False |
| c <= f    | [X] True [ ] False |

### Exercício 3.3

![alt text](../../imgs/Atividade%2002/image-3.png)

#### Resolução

| Expressão | Resultado          |
|-----------|--------------------|
| a and a   | [X] True [ ] False |
| b and b   | [ ] True [X] False |
| not c     | [ ] True [X] False |
| not b     | [X] True [ ] False |
| not a     | [ ] True [X] False |
| a and b   | [ ] True [X] False |
| b and c   | [ ] True [X] False |
| a or c    | [X] True [ ] False |
| b or c    | [X] True [ ] False |
| c or a    | [X] True [ ] False |
| c or b    | [X] True [ ] False |
| c or c    | [X] True [ ] False |
| b or b    | [ ] True [X] False |

### Exercício 3.5

![alt text](../../imgs/Atividade%2002/image-4.png)

#### Resolução

| A  | B  | C     | D     | Resultado |
|----|----|-------|-------|-----------|
| 1  | 2  | True  | False | False     |
| 10 | 3  | False | False | False     |
| 5  | 1  | True  | True  | True      |

### Exercício 3.6

![alt text](../../imgs/Atividade%2002/image-5.png)

#### Resolução

A expressão correspondente é: `Matéria1 > 7 and Matéria2 > 7 and Matéria3 > 7`

``` Python
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
```

Fonte: [exercício 3.6.py](exercícios/exercício%203.6.py)


### Exercício 3.7

![alt text](../../imgs/Atividade%2002/image-6.png)

#### Resolução

``` Python
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
```

Fonte: [exercício 3.7.py](exercícios/exercício%203.7.py)

### Exercício 3.8

![alt text](../../imgs/Atividade%2002/image-7.png)

#### Resolução

``` Python
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
```

Fonte: [exercício 3.8.py](exercícios/exercício%203.8.py)

### Exercício 3.9

![alt text](../../imgs/Atividade%2002/image-8.png)

#### Resolução

``` Python
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
```

Fonte: [exercício 3.9.py](exercícios/exercício%203.9.py)

### Exercício 3.10

![alt text](../../imgs/Atividade%2002/image-9.png)

#### Resolução

``` Python
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
```

Fonte: [exercício 3.10.py](exercícios/exercício%203.10.py)

### Exercício 3.11

![alt text](../../imgs/Atividade%2002/image-10.png)

#### Resolução

``` Python
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
```

Fonte: [exercício 3.11.py](exercícios/exercício%203.11.py)
