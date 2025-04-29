import sys
from PyQt5.QtWidgets import *
from Categoria import Categoria  # Usa Categoria
from TelaCarro import TelaCarro  # Usa TelaCarro para interagir

class TelaCategoria(QMainWindow):

    def __init__(self, titulo="Tela Categoria", categorias=[], telaCarro=None):
        super().__init__()
        self.listaCategorias = categorias  # Recebe a lista compartilhada
        self.telaCarro = telaCarro  # Referência para atualizar a telaCarro

        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 200, 100)
        self.layout = QVBoxLayout()

        self.definirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect(self.__salvar)  # Conecta botão ao método privado __salvar
        self.layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def definirLayout(self):
        # Monta os campos da tela
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)

    def __salvar(self):
        # Cria e adiciona uma nova Categoria e atualiza a telaCarro
        nome = self.txtNome.text()
        if(nome != ""):
            cat = Categoria(nome)
            self.listaCategorias.append(cat)
            self.telaCarro.carregarCategorias()
        QMessageBox.information(self, "Categoria salva", str(cat))