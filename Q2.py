#Crie uma classe "Arvore" para inserir um novo valor em um nó de uma árvore binária.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerdo is None:
                no_atual.esquerdo = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerdo, valor)
        elif valor > no_atual.valor:
            if no_atual.direito is None:
                no_atual.direito = No(valor)
            else:
                self._inserir_recursivo(no_atual.direito, valor)

# Exemplo de uso:
arvore = Arvore()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
