from .models import Usuario

class Cadastro:

    def __init__(self):
        self.lista_usuarios = Usuario.objects.all()

    # Função para simular o cadastro (cria uma Classe de Usuarios e utiliza objetos e seus atributos)
    def realizar_cadastro(self, nome_empresa_cad: str, email_cad: str, senha_cad: str, confirmar_senha_cad: str) -> None:
        """
            -> Função utilizada para armazenar na lista de cadastrados (quer armazena objetos usuario),
            verifica se os valores que o usuário querem cadastras são válidos e se sim adiciona o novo
            objeto na lista de cadastrados.
        :return: Não retorna nada.
        """
        sair = False
        while True:
            nome = str(input('Digite o nome: ')).lower()
            if nome != '':
                while True:
                    senha = str(input('Digite sua senha: ')).lower()
                    if senha != '':
                        repetir_senhar = str(input('Digite a sua senha novamente: ')).lower()
                        if senha == repetir_senhar:
                            temp = usuario.Usuario(nome, senha)
                            self.lista_usuarios.adicionar_a_lista_cadastrados(temp)
                            sair = True
                            print('Sucesso ao realizar cadastro! :)')
                            break
                        else:
                            print('Por favor digite senhas iguais!')
                    else:
                        print('Por favor digite uma senha válida')
            else:
                print('Por favor preencha com um valor válido')
            if sair:
                break
