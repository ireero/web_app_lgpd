from django.shortcuts import render
<<<<<<< HEAD
from .modulos.login import Login
from .modulos.erro import Erro
from .modulos.cadastro import Cadastro
from .modulos.login import Login
from .modulos.erro import Erro
from .modulos.cadastro import Cadastrar
=======

from .forms import CadastroForm
from .login import Login
from .erro import Erro
from .cadastro import Cadastrar
>>>>>>> teste
from django.http import HttpResponseRedirect
from django.urls import reverse
from .modulos.respostas import Respostas
from .modulos.pontuacoes import Pontuacoes


def index(request):
    return render(request, 'quiz/index.html')

def quiz(request):
    context = {}
    respostas = Respostas()
    pont = Pontuacoes()

    if request.method == 'POST':
        for v in range(1, 10):
            respostas.lista_de_respostas.append(int(request.POST.get(f'stp_{v}_valor_selecao', None)))
        
        for p in range(0, 4): # Adiciona a quantidade de cada tipo de resposta que foi dada na lista respostas_qtd
            respostas.respostas_qtd.append(respostas.lista_de_respostas.count(p))


        if respostas.lista_de_respostas:
            pont.calculo_pontuacao_parcial(respostas.respostas_qtd)
            pont.calculo_estrela()
            context = {
                'pontuacao': round(pont.get_estrelas(), 2),
            }
            return render(request, 'quiz/resultado.html', context)

  

    return render(request, 'quiz/quiz.html')

def resultado(request):
    return render(request, 'quiz/resultado.html')


def login(request):
    context = {}
    error = Erro()

    if request.method == 'POST':

        log = Login()

        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)

        error.verificar_campos_vazios_login(email, senha)

        if error.erros:
            context['erros'] = error.erros
            print(context)

        if log.verificarLogin(email, senha) == 1:
            context = {}
            return HttpResponseRedirect(reverse('quiz'))

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

