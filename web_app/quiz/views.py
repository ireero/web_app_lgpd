from django.shortcuts import render
from .login import Login
from .erro import Erro
from .cadastro import Cadastro


def index(request):
    return render(request, 'quiz/index.html')

def quiz(request):
    return render(request, 'quiz/quiz.html')


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

    return render(request, 'quiz/login_register.html', context)


def cadastro(request):
    context = {}
    error = Erro()
    cad = Cadastro()

    if request.method == 'POST':

        nome_empresa_cad = request.POST.get('nome_empresa_cad', None)
        email_cad = request.POST.get('email_cad', None)
        senha_cad = request.POST.get('senha_cad', None)
        confirm_senha_cad = request.POST.get('confirm_senha_cad', None)

        if error.verificar_campos_vazios_cadastro(nome_empresa_cad, email_cad, senha_cad, confirm_senha_cad) == 1:
            cad.realizar_cadastro(nome_empresa_cad, email_cad, senha_cad, confirm_senha_cad)

    return render(request, 'quiz/cadastro.html', context)
