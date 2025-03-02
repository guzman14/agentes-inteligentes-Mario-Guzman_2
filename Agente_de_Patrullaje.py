import random
import time

class AgentePatrullaje:
    def __init__(self, size=5):
        self.size = size
        self.matriz = [["." for _ in range(size)] for _ in range(size)]
        self.agente_x, self.agente_y = 0, 0
        self.matriz[self.agente_x][self.agente_y] = "A"
        self.direccion = "derecha"

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(" ".join(fila))
        print("\n")

    def detectar_obstaculo(self):
        return random.choice([True, False])  # Simulación de obstáculos aleatorios

    def cambiar_direccion(self):
        self.direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])

    def mover_agente(self):
        for _ in range(10):  # Limitar el número de pasos de patrullaje
            self.matriz[self.agente_x][self.agente_y] = "."
            if self.detectar_obstaculo():
                print("🚧 ¡Obstáculo detectado! Cambiando dirección...")
                self.cambiar_direccion()
            
            if self.direccion == "derecha" and self.agente_y < self.size - 1:
                self.agente_y += 1
            elif self.direccion == "izquierda" and self.agente_y > 0:
                self.agente_y -= 1
            elif self.direccion == "abajo" and self.agente_x < self.size - 1:
                self.agente_x += 1
            elif self.direccion == "arriba" and self.agente_x > 0:
                self.agente_x -= 1
            
            self.matriz[self.agente_x][self.agente_y] = "A"
            self.mostrar_matriz()
            time.sleep(1)

if __name__ == "__main__":
    agente = AgentePatrullaje()
    agente.mostrar_matriz()
    agente.mover_agente()
