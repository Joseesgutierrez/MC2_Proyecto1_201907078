import tkinter as tk
import 

class Disco:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.texto = textos[tamaño - 1]  # Asignar texto predeterminado según el tamaño
        self.label = tk.Label(tk.Canvas, text=self.texto)

textos = ["MC2", "José", "Manuel", "Estrada", "Gutiérrez", "2019", "07078"]