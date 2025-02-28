class Fila:
    def __init__(self):
        self.itens = []

    def entrar_na_fila(self, item):
        """Adiciona um cliente na fila."""
        self.itens.append(item)

    def sair_da_fila(self):
        """Remove e retorna o próximo cliente da fila."""
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0
