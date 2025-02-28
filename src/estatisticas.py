class EstatisticasFila:
    @staticmethod
    def calcular_tempo_medio_espera(tempos_espera):
        """Calcula o tempo médio de espera."""
        if len(tempos_espera) == 0:
            return 0
        return sum(tempos_espera) / len(tempos_espera)

    @staticmethod
    def calcular_taxa_ocupacao(tempos_espera, tempo_total_simulacao):
        """Calcula a taxa de ocupação do servidor corretamente."""
        if tempo_total_simulacao == 0:
            return 0
        return (sum(tempos_espera) / tempo_total_simulacao) * 100

    @staticmethod
    def exibir_estatisticas(tempos_espera, tempo_total_simulacao):
        """Exibe as estatísticas da simulação."""
        tempo_medio = EstatisticasFila.calcular_tempo_medio_espera(tempos_espera)
        taxa_ocupacao = EstatisticasFila.calcular_taxa_ocupacao(tempos_espera, tempo_total_simulacao)

        print("\n=== Estatísticas da Simulação ===")
        print(f"Tempo médio de espera: {tempo_medio:.2f} segundos")
        print(f"Taxa de ocupação do servidor: {taxa_ocupacao:.2f}%")
