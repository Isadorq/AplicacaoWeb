from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=40, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=20)


    def __str__(self):
        return self.nome
    
class Token(models.Model):
    nome = models.CharField(max_length=100)
    criacao = models.DateField()
    insercao = models.DateField()
    desc = models.CharField(max_length=255)
    valor = models.DecimalField()

    def __str__(self):
        return self.nome