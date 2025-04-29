import sys
from PyQt5.QtWidgets import *
from TelaVeiculo import TelaVeiculo  # Herda da tela de veículo
from Carro import Carro  # Usa a classe Carro

class TelaCarro(TelaVeiculo):  # Herda TelaVeiculo para especializar para Carro
    def __init__(self, titulo="Tela Carro"):
        super().__init__(titulo)  # Chama o __init__ da classe mãe (TelaVeiculo)
        self.setGeometry(450, 150, 300, 300)  # Redefine o tamanho e posição da janela

    def definirLayout(self):
        super().definirLayout()  # Mantém o layout base de TelaVeiculo
        self.lblPortas = QLabel("Quantidade de portas: ")  # Adiciona nova label
        self.txtPortas = QLineEdit(self)  # Adiciona novo campo de entrada
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)

    def salvar(self):
        # Salva os dados informados na tela criando um objeto Carro
        modelo = self.txtModelo.text()
        ano = self.txtAno.text()
        if(ano != ""):
            ano = int(ano)
        portas = self.txtPortas.text()
        if portas != "":
            portas = int(portas)
        carro = Carro(modelo, ano, portas)  # Cria um Carro
        QMessageBox.information(self, "Carro salvo", str(carro))

