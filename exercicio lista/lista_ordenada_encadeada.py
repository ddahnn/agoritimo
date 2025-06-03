class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaOrdenada:
    def __init__(self):
        self.inicio = None

    def add(self, valor):
        nodo = No(valor)
        # Lista vazia: insere no início
        if self.inicio is None:
            self.inicio = nodo
        # Valor menor que o primeiro elemento: insere no início
        elif valor < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            aux = self.inicio.prox
            # Avança enquanto aux existir e o valor for maior que aux.dado
            while aux:
                ant = aux
                aux = aux.prox

            ant.prox = nodo
            nodo.prox = aux

    def imprimir(self):
        print("-------------------------------")
        if self.inicio is None:
            print("Lista Encadeada vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.prox


    def remover(self, valor):
        removeu = False
        if self.inicio is not None:
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu:
                print(f"Elemento {valor} removido com sucesso")
            else:
                print(f"{valor} não foi encontrado")
        self.imprimir()