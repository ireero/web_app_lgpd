class Respostas:

    # Lista onde as respostas que o usuário responder irão ficar armazenadas
    respostas_usuario = []
    # Lista de quantas vezes cada opção foi escolhida como resposta
    respostas_qtd = []

    def __init__(self):
        # Lista de respostas que estarão disponiveis para o usuário responder
        self.lista_de_respostas = ['1 - Não, mas estamos planejando essa avaliação.', '2 - Sim, avaliamos os processos, mas ainda não corrigimos os problemas encontrados.',
                    '3 - Sim, e já começamos a tomar providência e adequálas a LGPD', '4 - Não, não é necessário.']