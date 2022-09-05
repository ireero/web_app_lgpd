from django.shortcuts import render
from .models import Cadastro, Questao, Pergunta, OpcaoResposta
from .modulos.login import Login
from .forms import CadastroForm
from .modulos.login import Login
from .modulos.pontuacoes import Pontuacoes
from datetime import datetime


def index(request):
    '''
        -> A página index retorna somente a página HTML normal.
    '''
    return render(request, 'quiz/index.html')


def quiz(request, id_usuario):
    '''
        -> Essa view é ativada quando  o formulário de quiz é submetido.
        -> Essa view recebe um id_usuario que vem através da view de login.
    '''
    context = {}
    pont = Pontuacoes()

    if request.method == 'POST':
        # Quando um o método POST é chamado é criada uma lista de respostas vazia
        lista_respostas = []
        for v in range(1, 10):
            # A lista de resposta armazena todas as respostas que foram dadas no formulário do quiz.
            resposta = (int(request.POST.get(f'stp_{v}_valor_selecao', None))) # Cada resposta do formulário fica temporariamente armazenada nessa variavel
            lista_respostas.append(resposta) 
            q = Questao(data_de_envio=datetime.now(), resposta=resposta, empresa=Cadastro.objects.get(pk=id_usuario), pergunta=Pergunta.objects.get(pk=v), opcao_resposta=OpcaoResposta.objects.get(pk=resposta + 1))
            q.save()
            # A cada valor do for é criada uma Questao (model) que equivale a uma questão do quiz
        
        # Aqui é feito o calculo das pontuações
        pont.calculo_pontuacao_parcial(lista_respostas)  
        pont.calculo_estrela()
        
        # retorna valores filtrando p = Questao.objects.filter(empresa=Cadastro.objects.get(id=id_usuario), data_de_envio=datetime.now())

        context = {
            'estrelas': round(pont.get_estrelas(),2)
        }

        return render(request, 'quiz/resultado.html', context)

    return render(request, 'quiz/quiz.html')

def resultado(request):
    '''
        -> Essa página é utilizada somente para mostrar o resultado que é retornado da view quiz
    '''
    return render(request, 'quiz/resultado.html')


def login(request):
    '''
        -> Essa é a view de login que verifica as credenciais que estão sendo digitadas e vai validar 
        se o e-mail e senha estão corretos.
    '''
    fail = 0
    context = {
        'fail': fail
    }
    perguntas = Pergunta.objects.all()


    if request.method == 'POST':
        # Quando o formulário de login é enviado essa view recebe o valor de email e senha
        log = Login()

        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)

        # Aqui é utilizado o módulo de Login para verificar se o email e senha são válidos com usuários
        # cadastrados no banco de dados.
        if log.verificarLogin(email, senha) != 0:
            context = {
                'id_usuario': log.verificarLogin(email, senha),
                'fail' : fail
            }
            # Se sim o usuário é redirecionado para a página do quiz
            return render(request, 'quiz/quiz.html', context)
        else:
            fail = 1
            context = {
                'fail' : fail
            }
    # Se não o usuário e redirecionado novamente para a página de login onde pode tentar acesssar novamente.
    return render(request, 'quiz/login_register.html', context)


def cadastro(request):
    '''
        -> Essa é a view que realiza o cadastro de novos usuários no banco de dados
    '''
    human = 3

    if request.POST:
        form = CadastroForm(request.POST)

        if form.is_valid():
            # Se o formulário for validado pelo própio Django é verificado se a senha e confirmar senha são iguais
            if form.data['senha'] == form.data['confirmar_senha']:
                # Se for igual é salvo o novo usuário no Banco de dados
                cliente = form.save()
                form = CadastroForm()
                human = 1
        else:
            human = 0
    else:
        form = CadastroForm()

    context = {
    'form': form,
    'human': human
    }

    return render(request, 'quiz/cadastro.html', context)


def termo(request):
    return render(request, 'quiz/termo.html')

