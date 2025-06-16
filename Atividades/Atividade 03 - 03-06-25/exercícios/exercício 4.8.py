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