primeira_lista = []
segunda_lista = []

while True:
    elemento = input("Digite um elemento para a primeira lista (ou 'fim' para terminar): ")
    if elemento.lower() == 'fim':
        break
    primeira_lista.append(elemento)

while True:
    elemento = input("Digite um elemento para a segunda lista (ou 'fim' para terminar): ")
    if elemento.lower() == 'fim':
        break
    segunda_lista.append(elemento)

terceira_lista = primeira_lista + segunda_lista

print("\nPrimeira lista:", primeira_lista)
print("Segunda lista:", segunda_lista)
print("Terceira lista (junção das duas):", terceira_lista)