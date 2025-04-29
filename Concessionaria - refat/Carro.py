from Veiculo import Veiculo  # Importa a classe Veiculo do arquivo Veiculo.py

class Carro(Veiculo):  # Cria a classe Carro herdando de Veiculo
    def __init__(self, modelo=None, ano=2025, qtd=4):
        super().__init__(modelo, ano)  # Chama o construtor da classe Veiculo
        self.portas = qtd  # Adiciona o atributo exclusivo "portas" para Carro

    def __str__(self):
        # Retorna a representação em string do Carro, aproveitando o __str__ da classe Veiculo e adicionando a informação de portas
        return super().__str__() + "\nPortas: " + str(self.portas)
