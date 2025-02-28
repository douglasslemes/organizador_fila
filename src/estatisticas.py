class EstatisticasFila:
    @staticmethod
    def calcular_tempo_medio_espera(tempos_espera):
        """Calcula o tempo médio de espera dos clientes na fila."""
        if not tempos_espera:  # Verifica se a lista está vazia
            return 0
        return sum(tempos_espera) / len(tempos_espera)

    @staticmethod
    def calcular_taxa_ocupacao(tempos_atendimento, tempo_total_simulacao):
        """Calcula a taxa de ocupação do servidor com base no tempo total de atendimento."""
        if tempo_total_simulacao == 0:
            return 0
        tempo_total_ocupado = sum(tempos_atendimento)  # Tempo total que o servidor ficou ocupado
        return (tempo_total_ocupado / tempo_total_simulacao) * 100

    @staticmethod
    def exibir_estatisticas(tempos_espera, tempos_atendimento, tempo_total_simulacao):
        """Exibe as estatísticas da simulação."""
        tempo_medio_espera = EstatisticasFila.calcular_tempo_medio_espera(tempos_espera)
        taxa_ocupacao = EstatisticasFila.calcular_taxa_ocupacao(tempos_atendimento, tempo_total_simulacao)

        print("\n=== Estatísticas da Simulação ===")
        print(f"Tempo médio de espera: {tempo_medio_espera:.2f} segundos")
        print(f"Taxa de ocupação do servidor: {taxa_ocupacao:.2f}%")
