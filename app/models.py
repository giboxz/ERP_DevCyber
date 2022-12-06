from django.db import models

class Entradas(models.Model):
    dataCriacao = models.DateField()
    valor = models.FloatField()
    descricao = models.CharField(max_length=250)
    setor = models.CharField(max_length=150)

class Saidas(models.Model):
    dataCriacao = models.DateField()
    dataPagamento = models.DateField()
    valor = models.FloatField()
    descricao = models.CharField(max_length=250)
    setor = models.CharField(max_length=150)
