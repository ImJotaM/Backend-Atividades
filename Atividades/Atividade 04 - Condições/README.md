# Atividade 01 - 22-04-25

## Exercícios

 - [Exercício 4.8](#exercício-48)
 - [Exercício 4.9](#exercício-49)
 - [Exercício 4.10](#exercício-410)

### Exercício 4.8
![alt text](../../imgs/Atividade%2004%20-%20Condições/)
![alt text](../../imgs/Atividade%2004%20-%20Condições/image-1.png)

#### Resolução

``` Python
def get_value(msg):
    while True:
        value = input(msg)
        try:
            return float(value)
        except ValueError:
            print(f"'{value}' não é um valor numérico válido.")
            
num1 = get_value("Digite um número: ")
num2 = get_value("Digite outro número: ")

result = num1
while True:
    operation = input("Escolha uma operação [ + ][ - ][ * ][ / ]: ")
    match operation:
        case '+':
            result += num2
            break
        case '-':
            result -= num2
            break
        case '*':
            result *= num2
            break
        case '/':
            result /= num2
            break
        case _:
            print(f"Operação '{ operation }' não encontrada. Digite novamente...")

print(f"O resultado da expressão '{num1} {operation} {num2}' é {result}")
```

Fonte: [exercício 4.8.py](exercícios/exercício%204.8.py)

### Exercício 4.9

![alt text](../../imgs/Atividade%2004%20-%20Condições/image-2.png)

#### Resolução

``` Python
def get_value_float(msg):
    while True:
        value = input(msg)
        try:
            return float(value)
        except ValueError:
            print(f"'{value}' não é um valor numérico válido.")

def get_value_int(msg):
    while True:
        value = input(msg)
        try:
            return int(value)
        except ValueError:
            print(f"'{value}' não é um valor inteiro válido.")

house_price = get_value_float("Digite o preço da casa: ")
years = get_value_int("Digite em quantos anos a casa será paga: ")
salary = get_value_float("Digite o salário do comprador: ")

installment = house_price / years

if installment <= salary * 30 / 100:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo recusado.")
```

Fonte: [exercício 4.9.py](exercícios/exercício%204.9.py)

### Exercício 4.10

![alt text](../../imgs/Atividade%2004%20-%20Condições/image-3.png)

#### Resolução

``` Python
def get_value_float(msg):
    while True:
        value = input(msg)
        try:
            return float(value)
        except ValueError:
            print(f"'{value}' não é um valor numérico válido.")

kwh = get_value_float("Digite a quantidade de consumo em kWh: ")

value = kwh
while True:
    
    print("Escolha o tipo de instalação:")
    print()
    print(" - Residêncial [R]")
    print(" - Comércial [C]")
    print(" - Indústrial [I]")
    print()
    type = input("Digite sua escolha: ")
    
    match type:
        case 'R':
            value *= 0.4 if kwh <= 500 else 0.65
            break
        case 'C':
            value *= 0.55 if kwh <= 1000 else 0.60
            break
        case 'I':
            value *= 0.55 if kwh <= 5000 else 0.60
            break
        case _:
            print(f"Tipo de instalação '{type} não encontrado. Tente novamente...\n'")

type_dict = { 'R':"Residêncial", 'C':"Comércial", 'I':"Indústrial" }
print(f"O preço a se pagar pelo consumo de {kwh} kWh, com tipo o tipo de instalação '{type_dict.get(type)}' é de R$ {value:.2f}")
```

Fonte: [exercício 4.10.py](exercícios/exercício%204.10.py)