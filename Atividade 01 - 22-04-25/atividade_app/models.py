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