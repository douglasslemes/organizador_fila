import random
import time
from .fila import FilaAtendimento

class SimulacaoFila:
    def __init__(self, num_clientes=10, tempo_medio_atendimento=3):
        self.num_clientes = num_clientes
        self.tempo_medio_atendimento = tempo_medio_atendimento
        self.fila = FilaAtendimento()
        self.tempos_espera = []

    def gerar_clientes(self):
        """Gera clientes e adiciona na fila simulando um tempo de chegada aleatório."""
        for i in range(1, self.num_clientes + 1):
            tempo_chegada = random.randint(1, 5)
            time.sleep(tempo_chegada / 10)  # Simula um pequeno tempo real
            self.fila.adicionar_cliente(i)

    def atender_clientes(self):
        """Atende os clientes da fila e calcula os tempos de espera."""
        while self.fila.tamanho_fila() > 0:
            cliente = self.fila.atender_cliente()
            tempo_espera = random.randint(1, self.tempo_medio_atendimento)
            self.tempos_espera.append(tempo_espera)
            time.sleep(tempo_espera / 10)  # Simula atendimento real

    def rodar_simulacao(self):
        """Executa toda a simulação."""
        print("Iniciando simulação de fila...\n")
        self.gerar_clientes()
        self.atender_clientes()
        return self.tempos_espera
