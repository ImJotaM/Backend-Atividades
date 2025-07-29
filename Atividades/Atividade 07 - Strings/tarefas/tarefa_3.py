frase = input("Digite uma frase longa: ")
palavra_chave = input("Digite a palavra-chave a ser pesquisada: ")

frase_lower = frase.lower()
palavra_chave_lower = palavra_chave.lower()

print("\n--- Buscando ocorrências ---")
posicao_inicial = -1
while True:
    posicao_inicial = frase_lower.find(palavra_chave_lower, posicao_inicial + 1)
    
    if posicao_inicial == -1:
        break
        
    print(f"'{palavra_chave}' encontrado na posição: {posicao_inicial}")

total_ocorrencias = frase_lower.count(palavra_chave_lower)
print(f"\nTotal de ocorrências de '{palavra_chave}': {total_ocorrencias}")