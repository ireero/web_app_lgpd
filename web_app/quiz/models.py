from django.db import models


# Classe que será utilizada como objeto de configuração no banco de dados
class Usuario(models.Model):

    # Metodo para ao vizualisar o banco de dados seja mostrado cada dado com o atributo nome
    def __str__(self) -> None:
        return self.nome

    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    data = models.DateTimeField('date published')
    pontuacao_parcial = models.IntegerField(default=0)
    estrelas = models.IntegerField(default=0)
