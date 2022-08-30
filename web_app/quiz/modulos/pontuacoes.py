from ..models import Pergunta, Questao

class Pontuacoes:

    __estrelas = 0
    __pontuacao_parcial = 0
    
    def __init__(self) -> None:
        self.questao = Questao.objects.all()
        self.perguntas_pesos = Pergunta.objects.all()

    # Função utilizada para calcular a quantidade de estrelas que o usuário vai receber
    def calculo_estrela(self) -> None:
        """
            -> Função utilizada para calcular a quantidade de estrelas baseada no teste de adequação a LPGD.
        :return: Não retorna nada.
        """
        self.__estrelas = (5 * self.__pontuacao_parcial) / (9 * 2)  # Calculo das estrelas

    # Função utilizada para calcular a pontuação parcial do usuário (100% = 2 pontos, 50% = 1 ponto)
    def calculo_pontuacao_parcial(self, lista_respostas) -> None:
        """
            -> Função utilizada para calcular a pontuação parcial do usuário no teste de adequação
        :return: Não retorna nada
        """
        for pos, c in enumerate(lista_respostas):  # Esse for anda pela lista respostas_qtd e também pelo seu indice
            if c == 1 or c == 0:  # Verifica as respostas de 50%
                if self.perguntas_pesos.get(id=pos+1).pesos == 1:
                    self.__pontuacao_parcial += 1
                else:
                    self.__pontuacao_parcial += 2
            elif c == 2:  # Verifica a resposta de 100%
                if self.perguntas_pesos.get(id=pos+1).pesos == 1:
                    self.__pontuacao_parcial += 2
                else:
                    self.__pontuacao_parcial += 3

    # Retorna o valor de estrelas
    def get_estrelas(self):
        return self.__estrelas

    # Retorna o valor da pontuação parcial
    def get_pontuacao_parcial(self):
        return self.__pontuacao_parcial


