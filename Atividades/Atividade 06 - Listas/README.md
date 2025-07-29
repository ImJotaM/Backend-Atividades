# Atividade 01 - 29-07-25

## Exercícios

  - [Exercício 6.2](#exercício-62)
  - [Exercício 6.3](#exercício-63)
  - [Exercício 6.11](#exercício-611)
  - [Exercício 6.12](#exercício-612)
  - [Exercício 6.13](#exercício-613)
  - [Exercício 6.17](#exercício-617)
  - [Exercício 6.18](#exercício-618)

-----

### Exercício 6.2

Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

#### Resolução

```python
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
```

-----

Fonte: [exercício 6.2.py](exercícios/exercício%206.2.py)

### Exercício 6.3

Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

#### Resolução

```python
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
```

-----

Fonte: [exercício 6.3.py](exercícios/exercício%206.3.py)

### Exercício 6.11

Modifique o programa da listagem 6.15 usando for. Explique por que nem todos os while podem ser transformados em for.

#### Resolução

```python
L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)

print("\nElementos da lista:")
for e in L:
    print(e)
```

**Explicação:**

Nem todo laço `while` pode ser transformado diretamente em um `for` porque o `for` é projetado para iterar sobre uma sequência definida de elementos (como uma lista, uma string ou um `range`). O laço `while`, por outro lado, executa enquanto uma condição for verdadeira, o que o torna ideal para situações onde o número de iterações não é conhecido previamente, como no caso da leitura de dados do usuário até que uma condição de parada seja atingida (neste exemplo, digitar 0). O primeiro `while` do código original, que lê os números, é um exemplo clássico disso. Já o segundo `while`, que apenas imprime os elementos da lista já preenchida, foi facilmente substituído por um `for`, pois a lista `L` é uma sequência finita.

-----

Fonte: [exercício 6.11.py](exercícios/exercício%206.11.py)

### Exercício 6.12

Altere o programa da listagem 6.33 de forma a imprimir o menor elemento da lista.

#### Resolução

```python
L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print("O menor elemento da lista é:", minimo)
```

-----

Fonte: [exercício 6.12.py](exercícios/exercício%206.12.py)

### Exercício 6.13

A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

#### Resolução

```python
T = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = T[0]
maior = T[0]
soma = 0

for temperatura in T:
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
    soma += temperatura

media = soma / len(T)

print(f"A menor temperatura é: {menor}°C")
print(f"A maior temperatura é: {maior}°C")
print(f"A temperatura média é: {media:.2f}°C")
```

-----

Fonte: [exercício 6.13.py](exercícios/exercício%206.13.py)

### Exercício 6.17

Altere o programa da listagem 6.53 de forma a solicitar ao usuário o produto e a quantidade vendida. Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.

#### Resolução

```python
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

total = 0
print("Vendas:\n")

while True:
    produto_vendido = input("Digite o nome do produto (ou 'fim' para encerrar): ").lower()
    if produto_vendido == 'fim':
        break

    if produto_vendido in estoque:
        quantidade_vendida = int(input(f"Digite a quantidade de '{produto_vendido}' vendida: "))
        preco = estoque[produto_vendido][1]
        custo = preco * quantidade_vendida

        if quantidade_vendida <= estoque[produto_vendido][0]:
            print("%12s: %3d x %6.2f = %6.2f" % (produto_vendido, quantidade_vendida, preco, custo))
            estoque[produto_vendido][0] -= quantidade_vendida
            total += custo
        else:
            print(f"Estoque insuficiente de {produto_vendido}. Temos apenas {estoque[produto_vendido][0]} unidades.")
    else:
        print("Produto não encontrado no estoque.")

print("\nCusto total: %21.2f\n" % total)
print("Estoque atualizado:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
```

-----

Fonte: [exercício 6.17.py](exercícios/exercício%206.17.py)

### Exercício 6.18

Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida. Exemplo: O rato -\> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

#### Resolução

```python
frase = input("Digite uma frase: ")
contagem_caracteres = {}

for caractere in frase:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

print("Dicionário de contagem de caracteres:")
print(contagem_caracteres)
```

-----

Fonte: [exercício 6.18.py](exercícios/exercício%206.18.py)