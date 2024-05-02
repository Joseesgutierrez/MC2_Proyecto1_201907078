import tkinter as tk
from gui import GUI

def main():
    root = tk.Tk()  # Crear la ventana principal de Tkinter
    app = GUI(root)  # Crear la instancia de la clase GUI
    root.mainloop()  # Iniciar el bucle principal de eventos

if __name__ == "__main__":
    main()