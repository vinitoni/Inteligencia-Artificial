from semaforo import Semaforo

class SistemaRegras:
    def __init__(self, semaforos):
        self.semaforos = semaforos

    def aplicar_regras(self, fila_veiculos):
        for semaforo in self.semaforos:
            #Regra 1: Abrir se há mais de 3 veículos e o semáforo está fechado há mais de 10 segundos
            if len(fila_veiculos[semaforo.direcao]) > 3 and semaforo.tempo_fechado > 10:
                self.abrir_semaforo(semaforo)

            #Regra 2: Fechar após 15 segundos de aberto
            elif semaforo.tempo_aberto > 15:
                semaforo.fechar()

            #Regra 3: Abrir se fechado por mais de 20 segundos e há veículos esperando
            elif semaforo.tempo_fechado > 20 and len(fila_veiculos[semaforo.direcao]) > 0:
                self.abrir_semaforo(semaforo)

            #Regra 4: Fechar se não houver mais veículos
            elif len(fila_veiculos[semaforo.direcao]) == 0 and semaforo.estado == 'aberto':
                semaforo.fechar()

            # Atualizar tempos de abertura/fechamento
            semaforo.atualizar_tempo()

    def abrir_semaforo(self, semaforo):
        for s in self.semaforos:
            if s != semaforo:
                s.fechar()
        semaforo.abrir()
