class Semaforo:
    def __init__(self, direcao):
        self.direcao = direcao
        self.estado = 'fechado'  # 'aberto' ou 'fechado'
        self.tempo_aberto = 0
        self.tempo_fechado = 0

    def abrir(self):
        if self.estado == 'fechado':
            self.estado = 'aberto'
            self.tempo_aberto = 0
            print(f"Semáforo {self.direcao} ABERTO")

    def fechar(self):
        if self.estado == 'aberto':
            self.estado = 'fechado'
            self.tempo_fechado = 0
            print(f"Semáforo {self.direcao} FECHADO")

    def atualizar_tempo(self):
        if self.estado == 'aberto':
            self.tempo_aberto += 1
        else:
            self.tempo_fechado += 1
