from django.db import models


class Usuario(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)
    data = models.DateTimeField('date published')
    pontuacao_parcial = models.IntegerField(default=0)
    estrelas = models.IntegerField(default=0)
