iimport random
import time

class AgenteExplorador:
    def __init__(self, size=5):
        self.size = size
        self.matriz = [["." for _ in range(size)] for _ in range(size)]
        
        # Posición inicial del agente (esquina superior izquierda)
        self.agente_x, self.agente_y = 0, 0
        self.matriz[self.agente_x][self.agente_y] = "A"
        
        # Almacenar posiciones visitadas
        self.visitadas = set()
        self.visitadas.add((self.agente_x, self.agente_y))
    
    def mostrar_matriz(self):
        """Imprime la cuadrícula con la posición del agente."""
        for fila in self.matriz:
            print(" ".join(fila))
        print("\n")
    
    def mover_agente(self):
        """Mueve el agente explorando nuevas zonas hasta que no queden opciones."""
        movimientos = [(0,1), (1,0), (0,-1), (-1,0)]  # Derecha, abajo, izquierda, arriba
        while len(self.visitadas) < self.size * self.size:
            random.shuffle(movimientos)
            for dx, dy in movimientos:
                nuevo_x, nuevo_y = self.agente_x + dx, self.agente_y + dy
                if 0 <= nuevo_x < self.size and 0 <= nuevo_y < self.size and (nuevo_x, nuevo_y) not in self.visitadas:
                    self.matriz[self.agente_x][self.agente_y] = "V"  # Marcar como visitado
                    self.agente_x, self.agente_y = nuevo_x, nuevo_y
                    self.matriz[self.agente_x][self.agente_y] = "A"  # Nueva posición del agente
                    self.visitadas.add((self.agente_x, self.agente_y))
                    self.mostrar_matriz()
                    time.sleep(1)
                    break
        print("¡Exploración completa! 🚀")

if __name__ == "__main__":
    agente = AgenteExplorador()
    agente.mostrar_matriz()
    agente.mover_agente()

