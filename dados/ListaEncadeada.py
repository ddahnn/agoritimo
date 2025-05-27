from No import No

class ListaEncadeada:
    
    def __init__(self):
        self.inicio = None
        
    def add_No_Inicio(self, valor):
        nodo = No(valor)
        if self.inicio != None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.imprimnirLista()
        
    def add_No_Final(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        elif self.inicio.prox  is None:
            self.inicio.prox = nodo
        else:
            ant = self.inicio
            aux = self.inicio.prox
            while aux.prox is not None:
                ant = aux
                aux = aux.prox
                ant.prox = None
                self.imprimnirLista()
                
                
    def imprimnirLista(self):
        print("***************** ********************* ******************")
        if self.inicio is None:
            print("A lista encadeada está vazia")
        else:
            aux = self.inicio
            while aux :
                print(aux.dado)
                aux = aux.prox
            
            
    def remover_Do_Inicio(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            print("Elemento removido.")
        self.imprimnirLista()
        
        
    def remover_Do_Fim(self):
        if self.inicio is not None:
            if self.inicio.prox is None:
                self.inicio = None
            else:
                aux = self.inicio
                while aux.prox != None:
                    aux = aux.prox
                aux.prox = None    
                print("Elemento removido.")
            self.imprimnirLista()
        
        