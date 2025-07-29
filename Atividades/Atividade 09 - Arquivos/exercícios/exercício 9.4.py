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