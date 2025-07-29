def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers.append(int(line.strip()))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
    return numbers

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

with open('pares.txt', 'w') as f:
    f.write('2\n4\n6\n8\n10\n')

with open('ímpares.txt', 'w') as f:
    f.write('1\n3\n5\n7\n9\n')

pares = read_numbers_from_file('pares.txt')
ímpares = read_numbers_from_file('ímpares.txt')

todos_numeros = sorted(pares + ímpares)

write_numbers_to_file('pareseímpares.txt', todos_numeros)

print("Arquivos 'pares.txt' e 'ímpares.txt' foram lidos e combinados em 'pareseímpares.txt'.")
print("Conteúdo de 'pareseímpares.txt':")
with open('pareseímpares.txt', 'r') as f:
    print(f.read())