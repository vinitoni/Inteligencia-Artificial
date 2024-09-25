from semaforo import Semaforo

class SistemaRegras:
    def __init__(self, semaforos):
        self.semaforos = semaforos
        self.semaforo_atual = None  #Semáforo atualmente aberto

    def aplicar_regras(self, fila_veiculos):

        if self.semaforo_atual is None or self.semaforo_atual.tempo_aberto >= 10:

            #Seleciona o semáforo com a maior fila
            direcao_maior_fila = max(fila_veiculos, key=lambda direcao: len(fila_veiculos[direcao]))
            semaforo_prioritario = next((s for s in self.semaforos if s.direcao == direcao_maior_fila), None)

            #Abrir o semáforo prioritário se o tempo mínimo de troca passou
            if semaforo_prioritario and semaforo_prioritario != self.semaforo_atual:
                self.abrir_semaforo(semaforo_prioritario)

        for semaforo in self.semaforos:
            #Fechar o semáforo atual ficou aberto pelo tempo estimado (10 segundos)
            if semaforo == self.semaforo_atual and semaforo.tempo_aberto >= 10:
                semaforo.fechar()
                self.semaforo_atual = None  #Libera para abrir outro semáforo

            #Atualiza os tempos de aberto e fechado
            semaforo.atualizar_tempo()

    def abrir_semaforo(self, semaforo):
        #Fecha todos os outros semáforos antes de abrir o próximo prioritário
        for s in self.semaforos:
            if s != semaforo:
                s.fechar()
        semaforo.abrir()

        #Semáfaro atual para garantir que ele fique aberto por tempo mínimo (10 segundos)
        self.semaforo_atual = semaforo
