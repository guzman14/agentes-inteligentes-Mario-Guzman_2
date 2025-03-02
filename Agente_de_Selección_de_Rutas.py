import random

class AgenteSeleccionRutas:
    def __init__(self, size=5):
        self.size = size
        self.mapa = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
        self.inicio = (0, 0)
        self.meta = (size - 1, size - 1)

    def mostrar_mapa(self):
        """Muestra el mapa con valores de recompensa."""
        print("Mapa de recompensas:")
        for fila in self.mapa:
            print(" ".join(f"{v:2}" for v in fila))
        print()

    def buscar_mejor_ruta(self):
        """Encuentra la ruta con mayor utilidad usando búsqueda en profundidad."""
        def dfs(x, y, recompensa, camino):
            if (x, y) == self.meta:
                rutas.append((recompensa, camino[:]))  # Guardar ruta final
                return
            
            for dx, dy in [(0, 1), (1, 0)]:  # Solo derecha y abajo
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    dfs(nx, ny, recompensa + self.mapa[nx][ny], camino + [(nx, ny)])

        rutas = []
        dfs(0, 0, self.mapa[0][0], [(0, 0)])
        mejor_ruta = max(rutas, key=lambda x: x[0])  # Ruta con mayor recompensa
        
        return mejor_ruta

    def ejecutar(self):
        self.mostrar_mapa()
        recompensa, ruta = self.buscar_mejor_ruta()
        print("Ruta seleccionada con mayor utilidad:")
        for paso in ruta:
            print(paso, end=" -> ")
        print(f"\nUtilidad total: {recompensa}")

if __name__ == "__main__":
    agente = AgenteSeleccionRutas()
    agente.ejecutar()
