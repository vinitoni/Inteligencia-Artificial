import tkinter as tk
from tkinter import ttk
import time
import threading
from simulacao import SimulacaoTransito

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação de Trânsito Inteligente")
        self.simulacao = SimulacaoTransito()

        # Definir padding geral e grid da janela principal
        self.root.geometry('400x300')
        self.root.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.root.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Criação da interface gráfica
        self.criar_interface()

        # Variáveis de controle da simulação
        self.simulacao_ativa = False

    def criar_interface(self):
        # Título
        self.titulo = tk.Label(self.root, text="Simulação de Trânsito Inteligente", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=4, pady=10)

        # Semáforos (rótulos com cores) centralizados
        self.label_norte = tk.Label(self.root, text="Norte", bg="red", width=10, height=2)
        self.label_sul = tk.Label(self.root, text="Sul", bg="red", width=10, height=2)
        self.label_leste = tk.Label(self.root, text="Leste", bg="red", width=10, height=2)
        self.label_oeste = tk.Label(self.root, text="Oeste", bg="red", width=10, height=2)

        # Posicionamento dos semáforos
        self.label_norte.grid(row=1, column=1, sticky="n", pady=(10, 0))
        self.label_sul.grid(row=3, column=1, sticky="s", pady=(0, 10))
        self.label_leste.grid(row=2, column=2, sticky="e", padx=(0, 10))
        self.label_oeste.grid(row=2, column=0, sticky="w", padx=(10, 0))

        # Fila de veículos (rótulos) centralizados e com padding
        self.label_fila_norte = tk.Label(self.root, text="Fila Norte: 0")
        self.label_fila_sul = tk.Label(self.root, text="Fila Sul: 0")
        self.label_fila_leste = tk.Label(self.root, text="Fila Leste: 0")
        self.label_fila_oeste = tk.Label(self.root, text="Fila Oeste: 0")

        # Posicionamento das filas, usando sticky para centralizar corretamente
        self.label_fila_norte.grid(row=1, column=2, sticky="n", pady=(10, 0))
        self.label_fila_sul.grid(row=3, column=2, sticky="s", pady=(0, 10))
        self.label_fila_leste.grid(row=2, column=3, sticky="e", padx=(0, 10))
        self.label_fila_oeste.grid(row=2, column=1, sticky="w", padx=(10, 0))

        # Botões de controle, centralizados na parte inferior
        self.botao_iniciar = tk.Button(self.root, text="Iniciar Simulação", command=self.iniciar_simulacao)
        self.botao_iniciar.grid(row=4, column=0, columnspan=2, pady=10, sticky="e")

        self.botao_parar = tk.Button(self.root, text="Parar Simulação", command=self.parar_simulacao)
        self.botao_parar.grid(row=4, column=2, columnspan=2, pady=10, sticky="w")

    def iniciar_simulacao(self):
        if not self.simulacao_ativa:
            self.simulacao_ativa = True
            threading.Thread(target=self.atualizar_simulacao).start()

    def parar_simulacao(self):
        self.simulacao_ativa = False

    def atualizar_simulacao(self):
        while self.simulacao_ativa:
            fila_veiculos, semaforos = self.simulacao.simular_tick()

            # Atualizar as filas
            self.label_fila_norte.config(text=f"Fila Norte: {len(fila_veiculos['Norte'])}")
            self.label_fila_sul.config(text=f"Fila Sul: {len(fila_veiculos['Sul'])}")
            self.label_fila_leste.config(text=f"Fila Leste: {len(fila_veiculos['Leste'])}")
            self.label_fila_oeste.config(text=f"Fila Oeste: {len(fila_veiculos['Oeste'])}")

            # Atualizar o estado dos semáforos
            for semaforo in semaforos:
                cor = "green" if semaforo.estado == "aberto" else "red"
                if semaforo.direcao == 'Norte':
                    self.label_norte.config(bg=cor)
                elif semaforo.direcao == 'Sul':
                    self.label_sul.config(bg=cor)
                elif semaforo.direcao == 'Leste':
                    self.label_leste.config(bg=cor)
                elif semaforo.direcao == 'Oeste':
                    self.label_oeste.config(bg=cor)

            time.sleep(1)

# Executar interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
