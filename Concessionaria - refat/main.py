import sys
from PyQt5.QtWidgets import *
from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro
from TelaCategoria import TelaCategoria

app = QApplication(sys.argv)  # Cria uma aplicação Qt

telaVeiculo = TelaVeiculo("Cadastro de Veículo")  # Cria a tela de veículo
telaVeiculo.show()  # Exibe a tela

categorias = []  # Lista que armazenará categorias

telaCat = TelaCategoria("Cadastro de Categoria", categorias)  # Cria a tela de categorias

telaCarro = TelaCarro("Cadastro de Carro: ", categorias, telaCat)  # Cria a tela de carros

telaCarro.show()  # Exibe a tela de carros

sys.exit(app.exec_())  # Executa o loop da aplicação