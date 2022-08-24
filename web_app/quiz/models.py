from audioop import mul
from pyexpat import model
from tkinter import CASCADE
from django.db import models


# Classe que será utilizada como objeto de configuração no banco de dados
class Cadastro(models.Model):

    # Metodo para ao vizualisar o banco de dados seja mostrado cada dado com o atributo nome
    def __str__(self) -> None:
        return self.nome_empresa

    nome_empresa = models.CharField(max_length=100, blank=False, null=False)
    nome_colaborador = models.CharField(max_length=100, blank=False, null=False)
    funcao_colaborador = models.CharField(max_length=100)
    email_colaborador = models.EmailField(max_length=100, unique=True)
    whatsapp_colaborador = models.CharField(max_length=14, unique=True)
    senha = models.CharField(max_length=30, blank=False, null=False)
    termo_de_uso = models.BooleanField('Eu aceito os termos de uso', default=False)

class Quiz(models.Model):

    def __str__(self) -> str:
        return self.data_de_envio

    respostas_quiz = models.CharField(max_length=1, default=True, null=True)
    data_de_envio = models.DateTimeField('data de envio', null=True, blank=True)
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)


class Perguntas(models.Model):

    def __str__(self) -> str:
        return self.perguntas

    perguntas = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Respostas(models.Model):

    def __str__(self) -> str:
        return self.respostas

    respostas = models.CharField(max_length=125)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
