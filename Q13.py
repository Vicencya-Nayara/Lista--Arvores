#Escreva uma função que retorna todos os nós em um determinado nível da árvore.

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

    def nos_no_nivel(self, nivel):
        nos = []
        self.encontrar_nos_no_nivel(self.raiz, nivel, nos)
        return nos

    def encontrar_nos_no_nivel(self, no, nivel_atual, nos):
        if no is None:
            return

        if nivel_atual == 0:
            nos.append(no.valor)
        else:
            self.encontrar_nos_no_nivel(no.esquerda, nivel_atual - 1, nos)
            self.encontrar_nos_no_nivel(no.direita, nivel_atual - 1, nos)

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

nivel_desejado = 2
nos_no_nivel = arvore.nos_no_nivel(nivel_desejado)
print(f"Nós no nível {nivel_desejado}: {nos_no_nivel}")
