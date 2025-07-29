# Atividade 03 - 29-07-25

## Exercícios

  - [Exercício 8.1](#exercício-81)
  - [Exercício 8.2](#exercício-82)
  - [Exercício 8.3](#exercício-83)
  - [Exercício 8.4](#exercício-84)

-----

### Exercício 8.1

Escreva uma função que retorne o maior de dois números.

**Valores esperados:**

  - `máximo(5,6) == 6`

  - `máximo(2,1) == 2`

  - `máximo(7,7) == 7`

#### Resolução

```python
def maximo(a, b):
  if a > b:
    return a
  else:
    return b

print(f"máximo(5, 6) -> Retorna: {maximo(5, 6)}, Esperado: 6")
print(f"máximo(2, 1) -> Retorna: {maximo(2, 1)}, Esperado: 2")
print(f"máximo(7, 7) -> Retorna: {maximo(7, 7)}, Esperado: 7")
```

-----

Fonte: [exercício 8.1.py](exercícios/exercício%208.1.py)

### Exercício 8.2

Escreva uma função que receba dois números e retorne `True` se o primeiro número for múltiplo do segundo.

**Valores esperados:**

  - `múltiplo(8,4) == True`

  - `múltiplo(7,3) == False`
  
  - `múltiplo(5,5) == True`

#### Resolução

```python
def multiplo(a, b):
  return a % b == 0

print(f"múltiplo(8, 4) -> Retorna: {multiplo(8, 4)}, Esperado: True")
print(f"múltiplo(7, 3) -> Retorna: {multiplo(7, 3)}, Esperado: False")
print(f"múltiplo(5, 5) -> Retorna: {multiplo(5, 5)}, Esperado: True")
```

-----

Fonte: [exercício 8.2.py](exercícios/exercício%208.2.py)

### Exercício 8.3

Escreva uma função que receba o lado (l) de um quadrado e retorne sua área ($A = lado^2$).

**Valores esperados:**

  - `área_quadrado(4) == 16`

  - `área_quadrado(9) == 81`

#### Resolução

```python
def area_quadrado(l):
  return l ** 2

print(f"área_quadrado(4) -> Retorna: {area_quadrado(4)}, Esperado: 16")
print(f"área_quadrado(9) -> Retorna: {area_quadrado(9)}, Esperado: 81")
```

-----

Fonte: [exercício 8.3.py](exercícios/exercício%208.3.py)

### Exercício 8.4

Escreva uma função que receba a base e a altura de um triângulo e retorne sua área ($A = \\frac{\\text{base} \\times \\text{altura}}{2}$).

**Valores esperados:**
 
  - `área_triângulo(6,9) == 27`
  
  - `área_triângulo(5,8) == 20`

#### Resolução

```python
def area_triangulo(base, altura):
  return (base * altura) / 2

print(f"área_triângulo(6, 9) -> Retorna: {area_triangulo(6, 9)}, Esperado: 27")
print(f"área_triângulo(5, 8) -> Retorna: {area_triangulo(5, 8)}, Esperado: 20")
```

-----

Fonte: [exercício 8.4.py](exercícios/exercício%208.4.py)