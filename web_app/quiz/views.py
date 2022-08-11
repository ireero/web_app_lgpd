from django.shortcuts import render
from . import models
from .login import Login


def index(request):
    return render(request, 'quiz/index.html')


def login(request):

    context = {}

    if request.method == 'POST':

        log = Login()

        erros = {}

        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)

        # Verifica se os campos estão vazios
        if email == '' and senha == '':
            erros['erro'] = 'Por favor insira algo para validação!'

        elif email == '':
            erros['erro'] = 'Por favor insira um e-mail válido!'

        elif senha == '':
            erros['erro'] = 'Por favor insira uma senha válida'

        if erros:
            context['erros'] = erros

        print(f'O email digitado foi: {email}\nA senha digitada foi: {senha}')
        log.verificarLogin(email, senha)
    return render(request, 'quiz/login_register.html', context)

