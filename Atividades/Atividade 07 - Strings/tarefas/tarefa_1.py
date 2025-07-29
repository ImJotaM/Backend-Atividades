string_original = input("Digite a string original: ")
try:
    indice = int(input("Digite o índice para a alteração: "))
    novo_caractere = input("Digite o novo caractere: ")

    if 0 <= indice < len(string_original):
        lista_caracteres = list(string_original)
        
        lista_caracteres[indice] = novo_caractere
        
        nova_string = "".join(lista_caracteres)
        
        print(f"String original: \"{string_original}\"")
        print(f"Nova string: \"{nova_string}\"")
    else:
        print(f"Erro: O índice {indice} está fora dos limites da string.")

except ValueError:
    print("Erro: O índice deve ser um número inteiro.")