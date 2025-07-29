entrada = input("Digite os dados no formato 'SOBRENOME, NOME, CIDADE': ")

partes = entrada.split(',')

if len(partes) == 3:
    sobrenome = partes[0].strip()
    nome = partes[1].strip()
    cidade = partes[2].strip()

    saida_formatada = f"{nome} {sobrenome} (de {cidade})"
    
    print(f"Entrada: \"{entrada}\"")
    print(f"Saída formatada: \"{saida_formatada}\"")
else:
    print("Formato de entrada inválido. Use 'SOBRENOME, NOME, CIDADE'.")
