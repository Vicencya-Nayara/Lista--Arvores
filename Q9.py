#Escreva uma função para contar o número total de nós em uma árvore binária.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)

    def contar_nos(self):
        if self.raiz is None:
            return 0
        else:
            return self.contar_nos_recursivo(self.raiz)

    def contar_nos_recursivo(self, no):
        if no is None:
            return 0
        else:
            return 1 + self.contar_nos_recursivo(no.esquerda) + self.contar_nos_recursivo(no.direita)


arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

numero_de_nos = arvore.contar_nos()
print("Número total de nós na árvore binária:", numero_de_nos)
