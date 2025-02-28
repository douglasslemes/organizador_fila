import random
import queue

class FilaAtendimento:
    def __init__(self):
        self.fila = queue.Queue()

    def adicionar_cliente(self, cliente):
        """Adiciona um cliente na fila."""
        self.fila.put(cliente)
        print(f"Cliente {cliente} entrou na fila.")

    def atender_cliente(self):
        """Atende o próximo cliente na fila."""
        if not self.fila.empty():
            cliente = self.fila.get()
            print(f"Atendendo cliente {cliente}...")
            return cliente
        print("Fila vazia, aguardando clientes...")
        return None

    def tamanho_fila(self):
        """Retorna o tamanho da fila."""
        return self.fila.qsize()
