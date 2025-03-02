import random
import time

class AgentePatrullaje:
    def __init__(self, size=5):
        self.size = size
        self.matriz = [["." for _ in range(size)] for _ in range(size)]
        
        # Ruta de patrullaje (camino fijo)
        self.ruta = [(i, 2) for i in range(size)]  # Movimiento en la columna central
        self.posicion_actual = 0  # Índice en la ruta
        self.x, self.y = self.ruta[self.posicion_actual]
        self.matriz[self.x][self.y] = "A"

        # Posicionar un obstáculo aleatorio en la ruta
        self.obstaculo_x, self.obstaculo_y = random.choice(self.ruta)
        while (self.obstaculo_x, self.obstaculo_y) == (self.x, self.y):
            self.obstaculo_x, self.obstaculo_y = random.choice(self.ruta)
        self.matriz[self.obstaculo_x][self.obstaculo_y] = "X"

    def mostrar_matriz(self):
        """Muestra la cuadrícula actual."""
        for fila in self.matriz:
            print(" ".join(fila))
        print("\n")

    def mover_agente(self):
        """Mueve el agente a lo largo de la ruta, esquivando obstáculos."""
        while True:
            # Borrar posición anterior
            self.matriz[self.x][self.y] = "."
            
            # Verificar si hay un obstáculo
            if (self.x, self.y) == (self.obstaculo_x, self.obstaculo_y):
                print("🚧 ¡Obstáculo detectado! Cambiando dirección...")
                self.x = random.randint(0, self.size - 1)  # Movimiento aleatorio en X
                self.y = random.randint(0, self.size - 1)  # Movimiento aleatorio en Y
            else:
                # Avanzar en la ruta predefinida
                self.posicion_actual = (self.posicion_actual + 1) % len(self.ruta)
                self.x, self.y = self.ruta[self.posicion_actual]
            
            # Actualizar posición del agente
            self.matriz[self.x][self.y] = "A"
            self.mostrar_matriz()
            time.sleep(1)  # Pausa para visualizar el movimiento

if __name__ == "__main__":
    agente = AgentePatrullaje()
    agente.mostrar_matriz()
    agente.mover_agente()
