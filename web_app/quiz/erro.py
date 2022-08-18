
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

    def verificar_campos_vazios_cadastro(self, nome_empresa, email, senha, confirmar_senha) -> int:

        # Verifica se os campos estão vazios
        if email == '' and senha == '' and nome_empresa == '' and confirmar_senha == '':
            self.erros['erro'] = 'Por favor insira algo para validação!'
            return 0
        elif nome_empresa == '':
            self.erros['erro'] = 'Por favor insira o nome da empresa!'
            return 0
        elif email == '':
            self.erros['erro'] = 'Por favor insira um e-mail válido!'
            return 0
        elif senha == '':
            self.erros['erro'] = 'Por favor insira uma senha válida'
            return 0
        elif confirmar_senha == '':
            self.erros['erro'] = 'Por favor confirme a sua senha!'
            return 0
        return 1
