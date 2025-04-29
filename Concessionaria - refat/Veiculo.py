# Intalando pacotes:
# python -m pip install --upgrade pip --user
# pip install pyqt5


# Veiculo.py
class Veiculo:
    def __init__(self, modelo=None, ano=2025):
        self.modelo = modelo  # Atributo do veículo: modelo
        self.ano = ano  # Atributo do veículo: ano

    def __str__(self):
        # Retorna a representação em string do Veiculo
        return f"Modelo: {self.modelo}\nAno: {self.ano}"
