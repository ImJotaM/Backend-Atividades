primeira_lista = [1, 2, 3, 4, 5]
segunda_lista = [4, 5, 6, 7, 8]
terceira_lista = []

for elemento in primeira_lista:
    if elemento not in terceira_lista:
        terceira_lista.append(elemento)

for elemento in segunda_lista:
    if elemento not in terceira_lista:
        terceira_lista.append(elemento)

print("Primeira lista:", primeira_lista)
print("Segunda lista:", segunda_lista)
print("Terceira lista (sem elementos repetidos):", terceira_lista)