# Escreva uma função que verifica se uma árvore binária é uma árvore de busca válida.

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

    def eh_arvore_de_busca(self):
        return self.verificar_arvore_de_busca(self.raiz, float('-inf'), float('inf'))

    def verificar_arvore_de_busca(self, no, min_valor, max_valor):
        if no is None:
            return True

        if not (min_valor < no.valor < max_valor):
            return False

        return (self.verificar_arvore_de_busca(no.esquerda, min_valor, no.valor) and
                self.verificar_arvore_de_busca(no.direita, no.valor, max_valor))

arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

eh_valida = arvore.eh_arvore_de_busca()
if eh_valida:
    print("A árvore é uma árvore de busca binária válida.")
else:
    print("A árvore não é uma árvore de busca binária válida.")
