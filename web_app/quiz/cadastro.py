from .models import Cadastro
from django.utils import timezone

class Cadastrar:

    def __init__(self):
        self.lista_usuarios = Cadastro.objects.all()

    # Função para realizar o cadastro do usuário no banco de dados
    def realizar_cadastro(self, nome_empresa_cad: str, email_cad: str, senha_cad: str, confirmar_senha_cad: str) -> None:

        if senha_cad == confirmar_senha_cad and self.__verificar_se_usuario_existe(email_cad) == 1:
            temp = Cadastro(nome=nome_empresa_cad, senha=senha_cad, email=email_cad, data=timezone.now())
            temp.save()
            # 'Sucesso ao realizar cadastro! :)

    def __verificar_se_usuario_existe(self, email_cad) -> int:

        for usuario in self.lista_usuarios:
            if usuario.email == email_cad:
                # Usuario já existe
                return 0
            # Usuario não existe
            return 1