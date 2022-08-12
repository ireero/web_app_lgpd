
class Erro:

    erros = {}

    def __int__(self):
        self.erros = {}

    def verificar_campos_vazios_login(self, email, senha) -> None:

        # Verifica se os campos estão vazios
        if email == '' and senha == '':
            self.erros['erro'] = 'Por favor insira algo para validação!'

        elif email == '':
            self.erros['erro'] = 'Por favor insira um e-mail válido!'

        elif senha == '':
            self.erros['erro'] = 'Por favor insira uma senha válida'

    def verificar_campos_vazios_cadastro(self, nome_empresa, email, senha, confirmar_senha) -> None:

        # Verifica se os campos estão vazios
        if email == '' and senha == '' and nome_empresa == '' and confirmar_senha == '':
            self.erros = 'Por favor insira algo para validação!'
        elif nome_empresa == '':
            self.erros['erro'] = 'Por favor insira o nome da empresa!'
        elif email == '':
            self.erros['erro'] = 'Por favor insira um e-mail válido!'
        elif senha == '':
            self.erros['erro'] = 'Por favor insira uma senha válida'
        elif confirmar_senha == '':
            self.erros['erro'] = 'Por confirme a sua senha!'
        else:
            self.erros['erro'] = 'Por favor preencha todos os campos!'
