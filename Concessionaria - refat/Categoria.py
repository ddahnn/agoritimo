class Categoria:
    def __init__(self, nome=None):
        self.nome = nome  # Inicializa o atributo nome da Categoria

    def __str__(self):
        # Retorna uma representação textual simples da Categoria
        return f"Nome:  {self.nome}"