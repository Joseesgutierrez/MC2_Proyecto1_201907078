import tkinter as tk
from torresHanoi import TorresDeHanoi

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Torres de Hanoi")
        
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        num_discos = self.solicitar_cantidad_discos()  # Solicitar cantidad de discos al usuario
        self.juego = TorresDeHanoi(self.canvas, num_discos)  # Iniciar el juego con la cantidad de discos
        
        self.juego = TorresDeHanoi(self.canvas)
        
        self.canvas.bind("<Button-1>", self.click)
        self.poste_seleccionado = None 

    def click(self, event):
        x, y = event.x, event.y
        poste = (x - 100) // 200  # Determinar sobre qué poste se hizo clic
        if poste in (0, 1, 2):
            if self.poste_seleccionado is None:  # Verificar si no hay ningún poste seleccionado
                if self.juego.postes[poste]:  # Verificar si hay discos en el poste seleccionado
                    self.poste_seleccionado = poste  # Seleccionar el poste
            else:
                if self.juego.mover_disco(self.poste_seleccionado, poste):  # Intentar mover el disco
                    self.juego.dibujar_postes()  # Actualizar la vista
                    self.poste_seleccionado = None  # Reiniciar el poste seleccionado
                    
def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
