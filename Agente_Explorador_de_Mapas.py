import random
import time

class AgenteExplorador:
    def __init__(self, size=5):
        self.size = size
        self.matriz = [["." for _ in range(size)] for _ in range(size)]
        
        # Posición inicial del agente
        self.x, self.y = 0, 0
        self.matriz[self.x][self.y] = "A"
        
        # Memoria de posiciones visitadas
        self.visitadas = set()
        self.visitadas.add((self.x, self.y))

    def mostrar_mapa(self):
        """Imprime la cuadrícula con la posición del agente."""
        for fila in self.matriz:
            print(" ".join(fila))
        print("\n")

    def posibles_movimientos(self):
        """Determina los movimientos posibles evitando celdas ya visitadas."""
        movimientos = []
        if self.x > 0 and (self.x - 1, self.y) not in self.visitadas:
            movimientos.append((-1, 0))  # Arriba
        if self.x < self.size - 1 and (self.x + 1, self.y) not in self.visitadas:
            movimientos.append((1, 0))   # Abajo
        if self.y > 0 and (self.x, self.y - 1) not in self.visitadas:
            movimientos.append((0, -1))  # Izquierda
        if self.y < self.size - 1 and (self.x, self.y + 1) not in self.visitadas:
            movimientos.append((0, 1))   # Derecha
        return movimientos

    def mover_agente(self):
        """Mueve el agente explorando nuevas zonas hasta que no haya más opciones."""
        while True:
            movimientos = self.posibles_movimientos()
            if not movimientos:
                print("Exploración completa! 🚀")
                break
            
            # Elegir un movimiento aleatorio
            dx, dy = random.choice(movimientos)
            self.matriz[self.x][self.y] = "."  # Limpia la posición anterior
            self.x += dx
            self.y += dy
            self.matriz[self.x][self.y] = "A"
            self.visitadas.add((self.x, self.y))
            
            self.mostrar_mapa()
            time.sleep(1)

if __name__ == "__main__":
    agente = AgenteExplorador()
    agente.mostrar_mapa()
    agente.mover_agente()
