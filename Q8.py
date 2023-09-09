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

    def travessia_em_niveis(self):
        if self.raiz is None:
            return []

        fila = [self.raiz]
        valores = []

        while fila:
            no_atual = fila.pop(0)
            valores.append(no_atual.valor)

            if no_atual.esquerda is not None:
                fila.append(no_atual.esquerda)
            if no_atual.direita is not None:
                fila.append(no_atual.direita)

        return valores

arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

print("Travessia em Níveis:")
travessia_em_niveis = arvore.travessia_em_niveis()
print(travessia_em_niveis)
