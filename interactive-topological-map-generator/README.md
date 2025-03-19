# Generador Interactivo de Mapas Topológicos

## Descripción
Este proyecto es un sistema que genera mapas topológicos interactivos para varias rutas. Utiliza estructuras de grafos para representar conexiones y caminos, permitiendo la travesía usando algoritmos como Búsqueda en Anchura (BFS) y Búsqueda en Profundidad (DFS). El proyecto también incluye actualizaciones dinámicas al grafo y representación visual usando NetworkX y Matplotlib.

## Estructura del Proyecto
```
interactive-topological-map-generator
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── graph.py               # Define la clase Graph
│   ├── algorithms
│   │   ├── __init__.py        # Archivo de inicialización para el paquete de algoritmos
│   │   ├── bfs.py             # Implementación del algoritmo BFS
│   │   └── dfs.py             # Implementación del algoritmo DFS
│   ├── dynamic_updates.py      # Funciones para actualizaciones dinámicas del grafo
│   ├── visualization.py        # Visualización del grafo usando NetworkX
│   └── priority_queue.py       # Implementación de la clase PriorityQueue
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación del proyecto
```

## Instalación
Para configurar el proyecto, clona el repositorio e instala las dependencias requeridas:

```bash
git clone <repository-url>
cd interactive-topological-map-generator
pip install -r requirements.txt
```

## Uso
Para ejecutar la aplicación, ejecuta el siguiente comando:

```bash
python src/main.py
```

Esto inicializará el grafo, añadirá aristas y realizará travesías BFS y DFS. El grafo también será visualizado.

## Características
- **Representación de Grafos**: Soporta grafos dirigidos y no dirigidos.
- **Algoritmos de Travesía**: Implementa BFS y DFS para la travesía de grafos.
- **Actualizaciones Dinámicas**: Permite añadir y eliminar aristas dinámicamente.
- **Visualización de Grafos**: Utiliza NetworkX y Matplotlib para representar visualmente el grafo.

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, envía una solicitud de extracción o abre un problema para cualquier mejora o corrección de errores.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.