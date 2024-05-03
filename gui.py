import tkinter as tk
from tkinter import simpledialog, messagebox
from torresHanoi import TorresDeHanoi

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Torres de Hanoi")
        
        # Crear etiquetas de texto para cada poste
        self.label_poste1 = tk.Label(self.master, text="Poste1")
        self.label_poste1.grid(row=0, column=0, padx=20)
        
        self.label_poste2 = tk.Label(self.master, text="Poste2")
        self.label_poste2.grid(row=0, column=1, padx=20)
        
        self.label_poste3 = tk.Label(self.master, text="Poste3")
        self.label_poste3.grid(row=0, column=2, padx=20)
        
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.grid(row=1, column=0, columnspan=3)  # Colocar el canvas debajo de las etiquetas
        
        self.btn_resolver = tk.Button(self.master, text="Resolver para n-discos", command=self.resolver_juego)
        self.btn_resolver.grid(row=2, column=0, pady=10)
        
        self.btn_reiniciar = tk.Button(self.master, text="Reiniciar", command=self.inicializar_juego)
        self.btn_reiniciar.grid(row=2, column=1, pady=10)

        self.btn_salir = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.btn_salir.grid(row=2, column=2, pady=10)


        num_discos = self.solicitar_cantidad_discos()
        self.juego = None  # Inicialmente no hay juego

        if num_discos:
            self.juego = TorresDeHanoi(self.canvas, num_discos)

        self.canvas.bind("<Button-1>", self.click)
        self.poste_seleccionado = None

    def resolver_juego(self):
        num_discosSolve = self.solicitar_cantidad_discos()
        if num_discosSolve is None:
            messagebox.showerror("Error", "Primero debes ingresar la cantidad de discos.")
            return
        else:        
            self.juego = TorresDeHanoi(self.canvas, num_discosSolve)  # Iniciar el juego con la cantidad de discos
            movimientos = self.juego.resolver_juego()  # Resolver el juego
            self.animar_movimientos(movimientos)  # Animar los movimientos


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
                if self.juego.validar_movimiento(self.poste_seleccionado, poste):  # Validar el movimiento
                    self.juego.mover_disco(self.poste_seleccionado, poste)  # Intentar mover el disco
                    self.juego.dibujar_postes()  # Actualizar la vista

                    if poste == 2 and len(self.juego.postes[2]) == self.juego.num_discos:
                        messagebox.showinfo("¡Éxito!", "¡Has completado el juego de las Torres de Hanoi!")
                else:
                    messagebox.showerror("Error", "No se puede mover un disco más grande sobre uno más pequeño.")
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
            self.master.after(200, self.animar_paso, movimientos, index + 1)  # Llamar a animar_paso después de 200 ms
        else:
            messagebox.showinfo("Movimientos", "Todos los movimientos han sido animados.")



    def main():
        root = tk.Tk()
        app = GUI(root)
        root.mainloop()

    if __name__ == "__main__":
        main()
