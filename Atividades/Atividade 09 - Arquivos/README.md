# Atividade 01 - 29-07-25

## Exercícios

 - [Exercício 9.3](#exercício-93)
 - [Exercício 9.4](#exercício-94)
 - [Exercício 9.5](#exercício-95)

-----

### Exercício 9.3

Crie um programa que leia os arquivos *pares.txt* e *ímpares.txt* e que crie um só arquivo *pareseímpares.txt* com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.

#### Resolução

```python
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
```

-----

Fonte: [exercício 9.3.py](exercícios/exercício%209.3.py)

### Exercício 9.4

Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando e que gere um arquivo de saída com as linhas do primeiro e do segundo arquivo.

#### Resolução

```python
import sys

def combine_files(file1_name, file2_name, output_file_name):
    try:
        with open(file1_name, 'r') as file1:
            content1 = file1.readlines()
        with open(file2_name, 'r') as file2:
            content2 = file2.readlines()

        with open(output_file_name, 'w') as output_file:
            output_file.writelines(content1)
            output_file.writelines(content2)
        print(f"Os arquivos '{file1_name}' e '{file2_name}' foram combinados em '{output_file_name}'.")
    except FileNotFoundError:
        print("Erro: Um ou ambos os arquivos de entrada não foram encontrados.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python seu_programa.py <arquivo1.txt> <arquivo2.txt> <arquivo_saida.txt>")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        output = sys.argv[3]
        
        with open(file1, 'w') as f:
            f.write('Linha A do arquivo 1\nLinha B do arquivo 1\n')
        with open(file2, 'w') as f:
            f.write('Linha X do arquivo 2\nLinha Y do arquivo 2\n')
            
        combine_files(file1, file2, output)
        print(f"Conteúdo de '{output}':")
        with open(output, 'r') as f:
            print(f.read())
```

-----

Fonte: [exercício 9.4.py](exercícios/exercício%209.4.py)

### Exercício 9.5

Crie um programa que inverta a ordem das linhas do arquivo *pares.txt*. A primeira linha deve conter o maior número; e a última, o menor.

#### Resolução

```python
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
```

-----

Fonte: [exercício 9.5.py](exercícios/exercício%209.5.py)