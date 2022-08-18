
class Pontuacoes:

    __estrelas = 0
    __pontuacao_parcial = 0

    # Função utilizada para calcular a quantidade de estrelas que o usuário vai receber
    def calculo_estrela(self) -> None:
        """
            -> Função utilizada para calcular a quantidade de estrelas baseada no teste de adequação a LPGD.
        :return: Não retorna nada.
        """
        self.__estrelas = (5 * self.__pontuacao_parcial) / (5 * 2)  # Calculo das estrelas

    # Função utilizada para calcular a pontuação parcial do usuário (100% = 2 pontos, 50% = 1 ponto)
    def calculo_pontuacao_parcial(self, lista_respostas_qtd) -> None:
        """
            -> Função utilizada para calcular a pontuação parcial do usuário no teste de adequação
        :return: Não retorna nada
        """
        for i, c in enumerate(lista_respostas_qtd):  # Esse for anda pela lista respostas_qtd e também pelo seu indice
            if (i == 0 and c >= 1) or (i == 1 and c >= 1):  # Verifica as respostas de 50%
                self.__pontuacao_parcial += (c * 1)
            elif i == 2 and c >= 1:  # Verifica a resposta de 100%
                self.__pontuacao_parcial += (c * 2)

    # Retorna o valor de estrelas
    def get_estrelas(self):
        return self.__estrelas

    # Retorna o valor da pontuação parcial
    def get_pontuacao_parcial(self):
        return self.__pontuacao_parcial


