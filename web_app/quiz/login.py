from .models import Cadastro


class Login:

    def __init__(self):
        self.lista_usuarios = Cadastro.objects.all()

    email_usuario_logado = 0

    # Função que verifica o usuário e senha
    def verificarLogin(self, email, pas) -> int:
        """
            -> Essa função é usada para verificações serão feitas de 1 por 1 em objetos armazenados na lista de usuários.
            Possui algumas prevenções a erros do usuário.
        :param email: Valor para confirmar o email do usuário
        :param pas:  Valor para confirmar a senha doe usuário
        :return:  Retorna um inteiro de 0 ou 1 (1 - para logado com sucesso e 0 - para falha no login)
        """
        for indice, valor in enumerate(self.lista_usuarios):
            email_verif = pas_verif = 0
            if valor.email == email:
                email_verif += 1
            if valor.senha == pas:
                pas_verif += 1
            if email_verif == 1 and pas_verif == 1:
                print('Parabéns você conseguiu efetuar o Login!')
                self.email_usuario_logado = email
                return 1
        # Verifica se o erro no login foi no usuário ou senha, até nos dois caso ambos estejam errados.
        if email_verif == 0 and pas_verif == 0:
            print('Email e senha incorretos!')
            return 0
        elif email_verif == 0 and pas_verif == 1:
            print('Email inválido! ')
            return 0
        elif email_verif == 1 and pas_verif == 0:
            print('Senha inválida! ')
            return 0