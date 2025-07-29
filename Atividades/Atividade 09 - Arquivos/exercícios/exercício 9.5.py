def reverse_and_sort_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        numbers = sorted([int(line.strip()) for line in lines if line.strip().isdigit()], reverse=True)
        reversed_content = [str(num) + '\n' for num in numbers]

        with open(filename, 'w') as file:
            file.writelines(reversed_content)
        print(f"O arquivo '{filename}' foi invertido (ordenado do maior para o menor).")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
    except ValueError:
        print(f"Erro: O arquivo '{filename}' contém linhas que não são números inteiros válidos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

with open('pares.txt', 'w') as f:
    f.write('2\n4\n6\n8\n10\n1\n3\n5\n7\n9\n')

reverse_and_sort_file('pares.txt')

print("Conteúdo de 'pares.txt' após a modificação:")
with open('pares.txt', 'r') as f:
    print(f.read())