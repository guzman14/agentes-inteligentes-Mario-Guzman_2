# Agentes Inteligentes en Python

Este repositorio contiene la implementación de cuatro agentes inteligentes desarrollados en Python, cada uno basado en diferentes enfoques de inteligencia artificial.

## 1. Agente de Patrullaje (Reflejo Simple)
**Descripción:** Un agente reflejo que patrulla una ruta predefinida, cambiando de dirección aleatoriamente si detecta un obstáculo.

**Características:**
- Se mueve siguiendo un camino fijo.
- Detecta obstáculos y cambia su dirección.
- Imprime sus movimientos en la consola.

## 2. Agente Explorador de Mapas (Con Estado Interno)
**Descripción:** Un agente que explora un entorno representado como una cuadrícula, recordando las áreas visitadas y evitando repetir caminos ya explorados.

**Características:**
- Representa el entorno como una matriz de celdas.
- Almacena en memoria las posiciones ya visitadas.
- Se mueve explorando nuevas zonas sin repetir.

## 3. Agente de Navegación Autónoma (Basado en Metas)
**Descripción:** Un agente que tiene como objetivo encontrar la salida en un laberinto de tamaño 5x5, buscando la ruta más corta para alcanzarla.

**Características:**
- Define un laberinto con paredes y una meta.
- Implementa un algoritmo de búsqueda para encontrar la salida.
- Muestra la ruta seguida por el agente.

## 4. Agente de Selección de Rutas (Basado en Utilidad)
**Descripción:** Un agente que selecciona la mejor ruta en un entorno con múltiples caminos y valores de recompensa, eligiendo el camino con mayor utilidad.

**Características:**
- Representa el entorno con valores de recompensa en cada celda.
- Implementa una función de utilidad para evaluar los caminos.
- Imprime el recorrido óptimo seleccionado por el agente.

## Ejecución
Cada agente puede ejecutarse de forma independiente con Python:
```sh
python agente_patrullaje.py
python agente_explorador_de_mapas.py
python agente_navegacion_Autonoma.py
python agente_seleccion_rutas.py
```

## Mejoras Realizadas
- Optimización en los algoritmos de búsqueda y selección de rutas.
- Mejor visualización de los movimientos de los agentes en la consola.
- Uso de estructuras de datos eficientes para mejorar el rendimiento.

