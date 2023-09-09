# Escreva uma função que, dado um nó, retorne todos os nós filhos do nó fornecido.

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

    def encontrar_filhos_de_no(self, no_alvo):
        filhos = []
        if no_alvo:
            if no_alvo.esquerda:
                filhos.append(no_alvo.esquerda)
            if no_alvo.direita:
                filhos.append(no_alvo.direita)
        return filhos

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

# Encontrar os filhos do nó com valor 3 (esquerda) e 7 (direita)
no_alvo = arvore.raiz.esquerda
filhos = arvore.encontrar_filhos_de_no(no_alvo)
if filhos:
    valores_filhos = [no.valor for no in filhos]
    print(f"Filhos do nó {no_alvo.valor}: {valores_filhos}")
else:
    print(f"O nó {no_alvo.valor} não possui filhos.")
