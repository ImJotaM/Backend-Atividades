# Atividade 01 - 29-07-25

## Exercícios

  - [Exercício 5.1](#exercício-51)
  - [Exercício 5.2](#exercício-52)
  - [Exercício 5.3](#exercício-53)
  - [Exercício 5.4](#exercício-54)
  - [Exercício 5.5](#exercício-55)

-----

### Exercício 5.1

Modifique o programa para exibir os números de 1 a 100.

#### Resolução

```python
x = 1
while x <= 100:
    print(x)
    x = x + 1
```

-----

Fonte: [exercício 5.1.py](exercícios/exercício%205.1.py)

### Exercício 5.2

Modifique o programa para exibir os números de 50 a 100.

#### Resolução

```python
x = 50
while x <= 100:
    print(x)
    x = x + 1
```

-----

Fonte: [exercício 5.2.py](exercícios/exercício%205.2.py)

### Exercício 5.3

Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo\! na tela.

#### Resolução

```python
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")
```

-----

Fonte: [exercício 5.3.py](exercícios/exercício%205.3.py)

### Exercício 5.4

Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

#### Resolução

```python
fim = int(input("Digite um número: "))
x = 1
while x <= fim:
    print(x)
    x = x + 2
```

-----

Fonte: [exercício 5.4.py](exercícios/exercício%205.4.py)

### Exercício 5.5

Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

#### Resolução

```python
x = 1
multiplos_encontrados = 0
while multiplos_encontrados < 10:
    if x % 3 == 0:
        print(x)
        multiplos_encontrados = multiplos_encontrados + 1
    x = x + 1
```

Fonte: [exercício 5.5.py](exercícios/exercício%205.5.py)