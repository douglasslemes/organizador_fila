import time
import random
from src.estatisticas import EstatisticasFila
from src.fila import Fila

def main():
    print("Iniciando simulação de fila...\n")

    fila = Fila()
    num_clientes = 10  # Número de clientes na simulação
    tempos_espera = []
    tempos_atendimento = []
    tempo_inicio_simulacao = time.time()

    # Simulação da chegada dos clientes
    for i in range(1, num_clientes + 1):
        print(f"Cliente {i} entrou na fila.")
        fila.entrar_na_fila(i)
        time.sleep(random.uniform(0.5, 1.5))  # Tempo aleatório entre chegadas

    # Simulação do atendimento dos clientes
    while not fila.esta_vazia():
        cliente = fila.sair_da_fila()
        tempo_inicio_atendimento = time.time()

        print(f"Atendendo cliente {cliente}...")

        tempo_atendimento = random.uniform(1, 3)  # Tempo aleatório de atendimento
        time.sleep(tempo_atendimento)

        tempo_fim_atendimento = time.time()
        tempo_espera = tempo_inicio_atendimento - tempo_inicio_simulacao
        tempos_espera.append(tempo_espera)
        tempos_atendimento.append(tempo_atendimento)

    tempo_total_simulacao = time.time() - tempo_inicio_simulacao

    # Exibir estatísticas da simulação
    EstatisticasFila.exibir_estatisticas(tempos_espera, tempos_atendimento, tempo_total_simulacao)

if __name__ == "__main__":
    main()
