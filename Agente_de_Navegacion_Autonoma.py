import os
from collections import deque

class AgenteNavegacion:
    def __init__(self):
        self.laberinto = [
            ["S", ".", "#", ".", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", ".", ".", "#", "."],
            ["#", "#", ".", ".", "E"]
        ]
        self.inicio = (0, 0)  # Posición de inicio 'S'
        self.meta = (4, 4)    # Posición de salida 'E'
        self.movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    def limpiar_pantalla(self):
        """Limpia la pantalla para mejorar la visualización de la exploración."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_laberinto(self, camino=[]):
        """Muestra el laberinto con el camino recorrido."""
        self.limpiar_pantalla()
        lab = [fila.copy() for fila in self.laberinto]
        for x, y in camino:
            if lab[x][y] not in ["S", "E"]:
                lab[x][y] = "*"

        for fila in lab:
            print(" ".join(fila))
        print("\n")

    def buscar_salida(self):
        """Encuentra la ruta más corta a la meta usando BFS."""
        print("🔍 Iniciando búsqueda de la salida...\n")
        queue = deque([(self.inicio, [self.inicio])])
        visitados = set()

        while queue:
            (x, y), camino = queue.popleft()
            self.mostrar_laberinto(camino)

            if (x, y) == self.meta:
                print(f"🚀 ¡Salida encontrada en {len(camino)-1} pasos!")
                return camino

            for dx, dy in self.movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and self.laberinto[nx][ny] != "#" and (nx, ny) not in visitados:
                    queue.append(((nx, ny), camino + [(nx, ny)]))
                    visitados.add((nx, ny))

        print("❌ No se encontró una salida.")
        return None

if __name__ == "__main__":
    agente = AgenteNavegacion()
    agente.mostrar_laberinto()
    agente.buscar_salida()

