# Atividade 01 - 22-04-25

## Instruções

1. [Definir os modelos do arquivo models.py (pelo menos 3 tabelas).](#definindo-os-modelos-do-arquivo-modelspy)

2. [Realizar migrações com makemigrations e migrate.](#realizando-migrações-com-makemigrations-e-migrate)

3. [Testar os modelos no shell do Django.](#testando-os-modelos-no-shell-do-django)

4. [Configurar conexão com o SQLite no DBeaver.](#configurando-conexão-com-o-sqlite-no-dbeaver)

5. [Inserir dados fictícios nas tabelas usando comandos SQL.](#inserindo-dados-fictícios-nas-tabelas-usando-comandos-sql)

6. [Verificar a estrutura e os dados das tabelas no DBeaver.](#verificando-a-estrutura-e-os-dados-das-tabelas-no-dbeaver)

## Definindo os modelos do arquivo models.py

Foram criados três modelos: [`Usuario`](atividade_app/models.py#L3), [`Vendedor`](atividade_app/models.py#L8) e [`Produto`](atividade_app/models.py#L13) dentro do arquivo [models.py](atividade_app/models.py).

```Python
# Implementação do arquivo models.py
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11)
    email = models.EmailField(null = True, default = None)
    
class Vendedor(models.Model):
    nome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11)
    email = models.EmailField(null = True, default = None)
    
class Produto(models.Model):
    nome = models.CharField(max_length = 100)
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)
    quantidade = models.IntegerField()
```

## Realizando migrações com makemigrations e migrate.

Os comandos a seguir foram utilizados para cumprir essa tarefa.

```
# Comando 'makemigrations'
python manage.py makemigrations

# Comando 'migrate'
python manage.py migrate
```

## Testando os modelos no shell do Django.

Para testar os modelos iremos utilizar o shell do Django, que pode ser inicializado com o comando abaixo.

```
// Comando para iniciar o shell do Django
python manage.py shell
```

Em seguida, importamos os modelos.

```Python
# Importando os modelos
>> from atividade_app.models import Usuario
>> from atividade_app.models import Vendedor
>> from atividade_app.models import Produto
```

Criamos então instâncias dos modelos e salvamos as mesmas.

```Python
# Criando instâncias dos modelos
>> novo_usuario  = Usuario ( nome = "Jeimes", "11111111111", "Jeimes@gmail.com" ) // E-mail opcional
>> novo_vendedor = Vendedor( nome = "Jonas",  "22222222222" )
>> novo_produto  = Produto ( nome = "Kwid" ,   79999.99, 10 )

# Salvando as instâncias
>> novo_usuario.save()
>> novo_vendedor.save()
>> novo_produto.save()
```

Verificamos então as instâncias salvas.

```Python
# Verificando as instâncias salvas
>> Usuario.objects.all()
>> Vendedor.objects.all()
>> Produto.objects.all()
```

## Configurando conexão com o SQLite no DBeaver.

Utilizando o Dbeaver, vamos fazer a conexão com o banco de dados.

Banco de Dados -> Nova conexão:

![alt text](../../imgs/Atividade%2001/image-1.png)

Selecionar o SQLite como banco de dados:

![alt text](../../imgs/Atividade%2001/image-2.png)

Selecionar o caminho para o banco de dados `db.sqlite3`.

![alt text](../../imgs/Atividade%2001/image-3.png)

## Inserindo dados fictícios nas tabelas usando comandos SQL.

Para inserir dados fictícios nas tabelas, utilizaremos um script SQL.

Editor SQL -> Novo script SQL

![alt text](../../imgs/Atividade%2001/image-4.png)

Agora com o script podemos adicionar os novos dados à tabela.

```SQL
INSERT INTO atividade_app_usuario ( nome, cpf, email )
VALUES ('Jeimes', '11111111111', 'Jeimes@gmail.com');

INSERT INTO atividade_app_vendedor ( nome, cpf )
VALUES ('Jonas', '22222222222');

INSERT INTO atividade_app_produto ( nome, preco, quantidade )
VALUES ('Kwid', 79999.99, 10);
```

## Verificando a estrutura e os dados das tabelas no DBeaver.

Para verificar a estrutura, basta clicar na tabela dentro do Navegador do banco de dados.

Tabela Usuario

![alt text](../../imgs/Atividade%2001/image-5.png)

Tabela Vendedor

![alt text](../../imgs/Atividade%2001/image-6.png)

Tabela Produto

![alt text](../../imgs/Atividade%2001/image-7.png)
