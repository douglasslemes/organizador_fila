from src.simulacao import SimulacaoFila
from src.estatisticas import EstatisticasFila
import time

if __name__ == "__main__":
    inicio = time.time()

    simulacao = SimulacaoFila(num_clientes=10, tempo_medio_atendimento=3)
    tempos_espera = simulacao.rodar_simulacao()

    fim = time.time()
    tempo_total_simulacao = fim - inicio

    EstatisticasFila.exibir_estatisticas(tempos_espera, tempo_total_simulacao)
