from tkinter import messagebox


class TorresDeHanoi:
    def __init__(self, canvas, num_discos):
        self.canvas = canvas
        self.postes = [list(range(num_discos, 0, -1)), [], []]  # Inicializar con la cantidad de discos deseada
        self.dibujar_postes()  # Dibujar postes y discos
        self.num_discos = num_discos  # Almacenar la cantidad de discos

    def resolver_juego(self):
        movimientos = []
        self.mover_torres(self.num_discos, 2, 0, 1, movimientos)
        return movimientos
    
    def dibujar_postes(self):
        # Código para dibujar postes y discos en el canvas
        # Limpiar canvas
        self.canvas.delete("all")
        
        # Dibujar postes
        for i in range(3):
            x0 = 100 + i * 200
            x1 = x0 + 20
            self.canvas.create_rectangle(x0, 100, x1, 300, fill="red")
        
        # Dibujar discos
        for i, poste in enumerate(self.postes):
            for j, disco in enumerate(poste):
                width = 20 + disco * 20
                x = 110 + i * 200 - width // 2
                y = 290 - j * 30
                self.canvas.create_rectangle(x, y, x + width, y + 10, fill="blue")
    
    def mover_disco(self, desde, hacia):
        if not self.postes[desde]:
            #print("No hay discos en el poste de origen.")
            return False
        elif self.postes[hacia] and self.postes[desde][-1] > self.postes[hacia][-1]:
            #messagebox.showerror("Error", "No se puede mover un disco más grande sobre uno más pequeño.")
            return False
        else:
            disco = self.postes[desde].pop()
            self.postes[hacia].append(disco)
            return True
        
    def mover_torres(self, n, origen, destino, auxiliar, movimientos):
        if n == 1:
            movimientos.append(f"Mover disco desde poste {origen + 1} hasta poste {destino + 1}")
            self.mover_disco(origen, destino)
        else:
            self.mover_torres(n-1, origen, auxiliar, destino, movimientos)
            movimientos.append(f"Mover disco desde poste {origen + 1} hasta poste {destino + 1}")
            self.mover_disco(origen, destino)
            self.mover_torres(n-1, auxiliar, destino, origen, movimientos)

        
