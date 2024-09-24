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

        self.root.geometry('400x300')
        self.root.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.root.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.criar_interface()

        self.simulacao_ativa = False

    def criar_interface(self):

        self.titulo = tk.Label(self.root, text="Simulação de Trânsito Inteligente", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=4, pady=10)

        self.label_1 = tk.Label(self.root, text="1", bg="red", width=10, height=2)
        self.label_2 = tk.Label(self.root, text="2", bg="red", width=10, height=2)
        self.label_3 = tk.Label(self.root, text="3", bg="red", width=10, height=2)
        self.label_4 = tk.Label(self.root, text="4", bg="red", width=10, height=2)

        #Posição dos semáforos
        self.label_1.grid(row=1, column=1, sticky="n", pady=(10, 0))
        self.label_2.grid(row=3, column=1, sticky="s", pady=(0, 10))
        self.label_3.grid(row=2, column=2, sticky="e", padx=(0, 10))
        self.label_4.grid(row=2, column=0, sticky="w", padx=(10, 0))

        self.label_fila_1 = tk.Label(self.root, text="Fila 1: 0")
        self.label_fila_2 = tk.Label(self.root, text="Fila 2: 0")
        self.label_fila_3 = tk.Label(self.root, text="Fila 3: 0")
        self.label_fila_4 = tk.Label(self.root, text="Fila 4: 0")

        self.label_fila_1.grid(row=1, column=2, sticky="n", pady=(10, 0))
        self.label_fila_2.grid(row=3, column=2, sticky="s", pady=(0, 10))
        self.label_fila_3.grid(row=2, column=3, sticky="e", padx=(0, 10))
        self.label_fila_4.grid(row=2, column=1, sticky="w", padx=(10, 0))

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

            self.label_fila_1.config(text=f"Fila 1: {len(fila_veiculos['1'])}")
            self.label_fila_2.config(text=f"Fila 2: {len(fila_veiculos['2'])}")
            self.label_fila_3.config(text=f"Fila 3: {len(fila_veiculos['3'])}")
            self.label_fila_4.config(text=f"Fila 4: {len(fila_veiculos['4'])}")

            for semaforo in semaforos:
                cor = "green" if semaforo.estado == "aberto" else "red"
                if semaforo.direcao == '1':
                    self.label_1.config(bg=cor)
                elif semaforo.direcao == '2':
                    self.label_2.config(bg=cor)
                elif semaforo.direcao == '3':
                    self.label_3.config(bg=cor)
                elif semaforo.direcao == '4':
                    self.label_4.config(bg=cor)

            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
