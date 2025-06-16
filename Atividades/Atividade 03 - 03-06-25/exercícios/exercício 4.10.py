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