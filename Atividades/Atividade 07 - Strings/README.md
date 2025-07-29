# Atividade 02 - 29-07-25

## Exercícios

  - [Tarefa 1](#tarefa-1)
  - [Tarefa 2](#tarefa-2)
  - [Tarefa 3](#tarefa-3)
  - [Tarefa 4](#tarefa-4)
  - [Tarefa 5](#tarefa-5)

-----

### Tarefa 1

**Manipulação de Caractere em String (Contornando a Imutabilidade)**

As strings em Python são imutáveis. Isso significa que você não pode alterar um caractere individual em uma posição específica diretamente, como faria em uma lista. Para realizar uma alteração caractere por caractere, é necessário primeiro transformar a string em uma lista, fazer a modificação na lista e, em seguida, converter a lista de volta para uma string.

**Tarefa:**

Escreva um programa em Python que:
 
 - Receba uma string original do usuário.

 - Receba um índice (número inteiro) onde a alteração deve ocorrer.

 - Receba um novo caractere que substituirá o caractere no índice especificado.
 
 - O programa deve substituir o caractere na string original no índice especificado pelo novo caractere e, em seguida, imprimir a nova string resultante.

 - Certifique-se de que seu código trate o caso de o índice estar fora dos limites da string (você pode optar por imprimir uma mensagem de erro nesse caso).

**Exemplo de uso:**

String original: "Python" Índice: 0 Novo caractere: 'J' Saída esperada: "Jython"

#### Resolução

```python
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

```

-----

Fonte: [tarefa_1.py](tarefas/tarefa_1.py)

### Tarefa 2

**Normalização e Validação de Nomes de Usuário**

Ao lidar com entradas de usuário, como nomes de usuário, é fundamental normalizar e validar os dados para garantir consistência e evitar problemas. Métodos como `strip()` podem remover espaços indesejados, `lower()` pode padronizar a capitalização, e métodos de validação como `isalnum()` podem verificar o tipo de conteúdo.

**Tarefa:**

Crie uma função Python chamada `validar_nome_usuario` que recebe uma string `nome_entrada` como parâmetro e realiza os seguintes passos:

 - **Normalização:** Primeiro, remova quaisquer espaços em branco do início ou fim da `nome_entrada` usando `strip()`. Em seguida, converta a string para minúsculas usando `lower()` para padronizar.

 - **Validação:** Após a normalização, verifique se a string resultante não está vazia e se consiste apenas de letras e/ou números. O método `isalnum()` é adequado para essa verificação, pois retorna `True` se todos os caracteres forem letras e/ou números, e `False` se contiver outros tipos de caracteres como espaços, vírgulas, etc..
 
 - A função deve retornar `True` se o nome de usuário for válido após a normalização e validação, e `False` caso contrário.

**Testes de exemplo (implemente no seu programa):**

 - `validar_nome_usuario(" Usuario123 ")` deve retornar `True`

 - `validar_nome_usuario("user_name")` deve retornar `False` (contém underscore)

 - `validar_nome_usuario("apenasletras")` deve retornar `True`

 - `validar_nome_usuario("12345")` deve retornar `True`

 - `validar_nome_usuario(" ")` deve retornar `False` (vazia após strip)

#### Resolução

```python
def validar_nome_usuario(nome_entrada):
    nome_normalizado = nome_entrada.strip().lower()
    
    if not nome_normalizado:
        return False
    
    if nome_normalizado.isalnum():
        return True
    else:
        return False

print(f"' Usuario123 ' -> {validar_nome_usuario(' Usuario123 ')}")
print(f"'user_name' -> {validar_nome_usuario('user_name')}")
print(f"'apenasletras' -> {validar_nome_usuario('apenasletras')}")
print(f"'12345' -> {validar_nome_usuario('12345')}")
print(f"' ' -> {validar_nome_usuario(' ')}")
print(f"'Com Espaços' -> {validar_nome_usuario('Com Espaços')}")

```

-----

Fonte: [tarefa_2.py](tarefas/tarefa_2.py)

### Tarefa 3

**Análise de Texto: Encontrando e Contando Palavras (Case-Insensitive)**

A busca e contagem de substrings são operações comuns na manipulação de texto. Para realizar essas operações sem se preocupar com a capitalização (maiúsculas ou minúsculas), é útil converter a string para um caso uniforme antes da pesquisa. Os métodos `find()` e `count()` são essenciais para isso.

**Tarefa:**

Escreva um programa em Python que:

 - Receba uma frase longa (string) do usuário.
 - Receba uma palavra-chave (substring) a ser pesquisada.
 - O programa deve encontrar todas as ocorrências da palavra-chave na frase, ignorando a diferença entre maiúsculas e minúsculas.

 - Para cada ocorrência encontrada, imprima a posição de início (índice).
 - Ao final, imprima o número total de vezes que a palavra-chave aparece na frase.

**Exemplo de uso:** 

Frase: "Este é um texto com texto repetido e Texto no final." Palavra-chave: "texto" Saída esperada: 'texto' encontrado na posição: 10 'texto' encontrado na posição: 23 'texto' encontrado na posição: 36 Total de ocorrências de 'texto': 3

#### Resolução

```python
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

```

-----

Fonte: [tarefa_3.py](tarefas/tarefa_3.py)

### Tarefa 4

**Reorganização de Dados Pessoais**

Strings frequentemente contêm dados estruturados que precisam ser reorganizados. Métodos como `split()` permitem dividir uma string em partes com base em um delimitador, e `join()` permite concatenar elementos de uma lista de volta em uma string.

**Tarefa:** 

Crie um programa que:

 - Receba uma string do usuário no formato "SOBRENOME, NOME, CIDADE" (por exemplo, "Silva, João, São Paulo").
 - O programa deve reformatar essa string para o formato "NOME SOBRENOME (de CIDADE)" (por exemplo, "João Silva (de São Paulo)").
 - Utilize o método `split()` para separar as partes da string.
 - Considere o uso de `strip()` em cada parte após a divisão para remover espaços em branco extras que podem surgir.
**Exemplo de uso:** Entrada: "Souza, Maria, Rio de Janeiro" Saída esperada: "Maria Souza (de Rio de Janeiro)"

#### Resolução

```python
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

```

-----

Fonte: [tarefa\_4.py](tarefas/tarefa_4.py)

### Tarefa 5

**Formatação Avançada de Relatórios Financeiros**

A formatação de strings é crucial para apresentar dados de forma clara e alinhada. A nova sintaxe do método `format()` e as f-strings em Python 3 oferecem poderosas opções para alinhamento, preenchimento e formatação numérica, inclusive levando em conta as configurações regionais.

**Tarefa:**

Dada a seguinte lista de produtos com seus respectivos preços:

`itens_venda = [("Produto A Longo Nome", 150.75), ("Item B", 25.00), ("C-123", 12345.80), ("Dígito Simples", 5.99)]`

Escreva um programa Python que imprima uma fatura formatada com as seguintes características:

 - A fatura deve ter um cabeçalho "Item" e "Preço" centralizado.
 - O nome do item deve ser alinhado à esquerda em uma coluna de 25 caracteres.
 - O preço deve ser alinhado à direita em uma coluna de 10 caracteres.
 - O preço deve ser formatado para duas casas decimais.
 - O preço deve usar o formato regional para separador de milhar (ponto) e decimal (vírgula). Para isso, você precisará configurar o `locale`.
 - Entre o cabeçalho e os itens, imprima uma linha separadora.

#### Resolução

```python
import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale 'pt_BR.UTF-8' não suportado. Usando o padrão do sistema.")
    locale.setlocale(locale.LC_ALL, '')

itens_venda = [
    ("Produto A Longo Nome", 150.75),
    ("Item B", 25.00),
    ("C-123", 12345.80),
    ("Dígito Simples", 5.99)
]

LARGURA_ITEM = 25
LARGURA_PRECO = 10
LARGURA_TOTAL = LARGURA_ITEM + LARGURA_PRECO + 1

print(f"{'Item':<{LARGURA_ITEM}} {'Preço':>{LARGURA_PRECO}}")
print('-' * LARGURA_TOTAL)

for item, preco in itens_venda:
    preco_formatado = locale.format_string('%.2f', preco, grouping=True)
    print(f"{item:<{LARGURA_ITEM}} {preco_formatado:>{LARGURA_PRECO}}")

```

-----

Fonte: [tarefa_5.py](tarefas/tarefa_5.py)