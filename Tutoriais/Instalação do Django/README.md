# Instalação do Django

O Django é um framework web Python de alto nível que incentiva o desenvolvimento rápido e o design limpo e pragmático.

## Instalações

 - [Instalação automática](#instalação-automática)
 - [Instalação manual](#instalação-manual)

## Instalação automática

Para fazer a instalação automática do django, utilize o [DjangoInstaller](InstallDjango.exe).

### DjangoInstaller

DjangoInstaller é um programa feito em python para instalar o framework Django de maneira simples e rápida. O software utiliza do gerenciador de pacotes Scoop para instalar o Python na máquina do usuário (caso o mesmo não o possua) e instala o Django aravés do `pip`. [Confira o código fonte aqui](InstallDjango.py).

![alt text](../../imgs/Tutorial%20-%20Instalação%20do%20Django/image.png)

## Instalação manual

Para a instalação do Django iremos primeiro instalar o `python` para acesso ao comando `pip` e em seguida utilizaremos o mesmo para instalação do `django`.

## Instalando o Python

### Windows

Para instalar o `python` no Windows, a maneira mais simples é através do gerenciador de pacotes `Scoop`.

Para instalar o Scoop em sua máquina, utilize os comandos a seguir dentro do seu `Powershell`:

```Powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

Para instalar o `python`, utilizaremos também dentro do powershell o comando a seguir:

```Powershell
scoop install python
```

## Instalando o Django

### Windows

Para instalar o Django em sua máquina, após a instalação do Python, utilize também no seu powershell o comando a seguir:

```Powershell
pip install django
```