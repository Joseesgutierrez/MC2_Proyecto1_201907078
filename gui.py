import tkinter as tk
from tkinter import simpledialog, messagebox
from torresHanoi import TorresDeHanoi

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Torres de Hanoi")
        
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        self.btn_resolver = tk.Button(self.master, text="Resolver", command=self.resolver_juego)
        self.btn_resolver.pack()

        self.btn_reiniciar = tk.Button(self.master, text="Reiniciar", command=self.inicializar_juego)
        self.btn_reiniciar.pack()
        
        num_discos = self.solicitar_cantidad_discos()  # Solicitar cantidad de discos al usuario
        self.juego = TorresDeHanoi(self.canvas, num_discos)  # Iniciar el juego con la cantidad de discos
        
        self.canvas.bind("<Button-1>", self.click)
        self.poste_seleccionado = None

    def resolver_juego(self):
        if not self.juego:
            self.inicializar_juego()
        movimientos = self.juego.resolver_juego()
        self.animar_movimientos(movimientos)

    def inicializar_juego(self):
        num_discos = self.solicitar_cantidad_discos()
        if num_discos:
            self.juego = TorresDeHanoi(self.canvas, num_discos)

    def solicitar_cantidad_discos(self):
        # Mostrar un cuadro de diálogo para que el usuario ingrese la cantidad de discos
        return simpledialog.askinteger("Cantidad de discos", "Ingrese la cantidad de discos (1-7):", minvalue=1, maxvalue=7)

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

    def animar_movimientos(self, movimientos):
        if movimientos:
            self.animar_paso(movimientos, 0)
        else:
            messagebox.showinfo("Movimientos", "No hay movimientos necesarios.")

    def animar_paso(self, movimientos, index):
        if index < len(movimientos):
            movimiento = movimientos[index]
            partes = movimiento.split(" ")
            origen, destino = int(partes[4])-1, int(partes[7])-1
            self.juego.mover_disco(origen, destino)
            self.juego.dibujar_postes()
            self.master.after(500, self.animar_paso, movimientos, index + 1)  # Llamar a animar_paso después de 1000 ms
        else:
            messagebox.showinfo("Movimientos", "Todos los movimientos han sido animados.")

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
