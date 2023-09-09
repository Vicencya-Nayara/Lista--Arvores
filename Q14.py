# Escreva uma função que encontre o caminho da raiz até um nó específico na árvore.

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

    def encontrar_caminho_ate_no(self, valor_alvo):
        caminho = []
        self.encontrar_caminho_recursivo(self.raiz, valor_alvo, caminho)
        return caminho

    def encontrar_caminho_recursivo(self, no, valor_alvo, caminho):
        if no is None:
            return False

        caminho.append(no.valor)

        if no.valor == valor_alvo:
            return True

        if (self.encontrar_caminho_recursivo(no.esquerda, valor_alvo, caminho) or
                self.encontrar_caminho_recursivo(no.direita, valor_alvo, caminho)):
            return True

        caminho.pop()
        return False

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

valor_alvo = 4
caminho = arvore.encontrar_caminho_ate_no(valor_alvo)
if caminho:
    print(f"Caminho da raiz até o nó {valor_alvo}: {caminho}")
else:
    print(f"Nó {valor_alvo} não encontrado na árvore.")
