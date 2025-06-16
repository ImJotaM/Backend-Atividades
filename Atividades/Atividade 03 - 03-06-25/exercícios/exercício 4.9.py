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