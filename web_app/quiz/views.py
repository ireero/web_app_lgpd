from django.shortcuts import render

from .models import Cadastro, Questao, Pergunta, OpcaoResposta
from .modulos.login import Login
from .forms import CadastroForm
from .modulos.login import Login
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .modulos.respostas import Respostas
from .modulos.pontuacoes import Pontuacoes
from datetime import datetime


def index(request):
    return render(request, 'quiz/index.html')


def quiz(request, id_usuario):
    context = {}
    pont = Pontuacoes()
    

    if request.method == 'POST':
        
        for v in range(1, 10):
            resposta = (int(request.POST.get(f'stp_{v}_valor_selecao', None)))
            q = Questao(data_de_envio=datetime.now(), resposta=resposta, empresa=Cadastro.objects.get(pk=id_usuario), pergunta=Pergunta.objects.get(pk=v), opcao_resposta=OpcaoResposta.objects.get(pk=resposta + 1))
            q.save()
            print(q)
        return render(request, 'quiz/resultado.html', context)

  
    return render(request, 'quiz/quiz.html')

def resultado(request):
    return render(request, 'quiz/resultado.html')


def login(request):
    context = {}
    perguntas = Pergunta.objects.all()

    if request.method == 'POST':

        log = Login()

        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)

        if log.verificarLogin(email, senha) != 0:
            context = {
                'id_usuario': log.verificarLogin(email, senha)
            }
            return render(request, 'quiz/quiz.html', context)

    return render(request, 'quiz/login_register.html', context)


def cadastro(request):
    context = {}


    form = CadastroForm(request.POST)

    if form.is_valid():
        cliente = form.save()
        form = CadastroForm()

    context = {
        'form': form
    }
    return render(request, 'quiz/cadastro.html', context)

