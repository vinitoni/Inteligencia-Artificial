from veiculo import Veiculo
from semaforo import Semaforo
from sistema_regras import SistemaRegras

class SimulacaoTransito:
    def __init__(self):
        self.semaforos = [
            Semaforo('Norte'),
            Semaforo('Sul'),
            Semaforo('Leste'),
            Semaforo('Oeste')
        ]
        self.regras = SistemaRegras(self.semaforos)
        self.fila_veiculos = {
            'Norte': [],
            'Sul': [],
            'Leste': [],
            'Oeste': []
        }

    def adicionar_veiculo(self, direcao):
        veiculo = Veiculo(direcao)
        self.fila_veiculos[direcao].append(veiculo)
        print(f"Veículo adicionado na fila {direcao}. Total: {len(self.fila_veiculos[direcao])} veículos.")

    def simular_tick(self):
        # Simular chegada aleatória de veículos
        import random
        direcao_aleatoria = random.choice(['Norte', 'Sul', 'Leste', 'Oeste'])
        self.adicionar_veiculo(direcao_aleatoria)

        # Aplicar regras de controle dos semáforos
        self.regras.aplicar_regras(self.fila_veiculos)

        # Simular passagem de veículos (remover veículo da fila se o semáforo estiver aberto)
        for semaforo in self.semaforos:
            if semaforo.estado == 'aberto' and len(self.fila_veiculos[semaforo.direcao]) > 0:
                self.fila_veiculos[semaforo.direcao].pop(0)
                print(f"Veículo passou pelo semáforo {semaforo.direcao}. Restam {len(self.fila_veiculos[semaforo.direcao])} veículos.")

        return self.fila_veiculos, self.semaforos
