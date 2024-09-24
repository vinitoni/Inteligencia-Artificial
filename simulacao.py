from veiculo import Veiculo
from semaforo import Semaforo
from sistema_regras import SistemaRegras

class SimulacaoTransito:
    def __init__(self):
        self.semaforos = [
            Semaforo('1'),
            Semaforo('2'),
            Semaforo('3'),
            Semaforo('4')
        ]
        self.regras = SistemaRegras(self.semaforos)
        self.fila_veiculos = {
            '1': [],
            '2': [],
            '3': [],
            '4': []
        }

    def adicionar_veiculo(self, direcao):
        veiculo = Veiculo(direcao)
        self.fila_veiculos[direcao].append(veiculo)
        print(f"Veículo adicionado na fila {direcao}. Total: {len(self.fila_veiculos[direcao])} veículos.")

    def simular_tick(self):
        #Simular chegada aleatória de veículos
        import random
        direcao_aleatoria = random.choice(['1', '2', '3', '4'])
        self.adicionar_veiculo(direcao_aleatoria)

        #Aplicar regras de controle dos semáforos
        self.regras.aplicar_regras(self.fila_veiculos)

        # Simular passagem de veículos (remover veículo da fila se o semáforo estiver aberto)
        for semaforo in self.semaforos:
            if semaforo.estado == 'aberto' and len(self.fila_veiculos[semaforo.direcao]) > 0:
                self.fila_veiculos[semaforo.direcao].pop(0)
                print(f"Veículo passou pelo semáforo {semaforo.direcao}. Restam {len(self.fila_veiculos[semaforo.direcao])} veículos.")

        return self.fila_veiculos, self.semaforos
