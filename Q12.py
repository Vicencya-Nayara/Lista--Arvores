#Implemente um método na classe `Arvore` que permite a remoção de um nó específico da árvore.

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if no is None:
            return Node(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_recursivo(no.direita, valor)
        return no

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            no.valor = self._encontrar_minimo_valor(no.direita)
            no.direita = self._remover_recursivo(no.direita, no.valor)

        return no

    def _encontrar_minimo_valor(self, no):
        while no.esquerda:
            no = no.esquerda
        return no.valor

    def em_ordem(self):
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _em_ordem_recursivo(self, no, resultado):
        if no:
            self._em_ordem_recursivo(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem_recursivo(no.direita, resultado)

# Exemplo de uso:
arvore = Arvore()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

print("Árvore antes da remoção:", arvore.em_ordem())
arvore.remover(2)
print("Árvore após a remoção:", arvore.em_ordem())
