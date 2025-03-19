# Interactive Topological Map Generator

## Description
This project generates interactive topological maps for various routes. It uses graph structures to represent connections and paths, allowing traversal using algorithms such as Breadth-First Search (BFS) and Depth-First Search (DFS). The project also includes dynamic updates to the graph and visual representation using NetworkX and Matplotlib.

## Project Structure
```
interactive-topological-map-generator
├── src
│   ├── main.py                # Application entry point
│   ├── graph.py               # Defines the Graph class
│   ├── algorithms
│   │   ├── __init__.py        # Initialization file for the algorithms package
│   │   ├── bfs.py             # Implementation of the BFS algorithm
│   │   └── dfs.py             # Implementation of the DFS algorithm
│   ├── dynamic_updates.py     # Functions for dynamic graph updates
│   ├── visualization.py       # Graph visualization using NetworkX
│   └── priority_queue.py      # Implementation of the PriorityQueue class
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <[repository-url](https://github.com/cyberwarrior8/Interactive-Graphs.git)>
cd interactive-topological-map-generator
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:

```bash
python src/main.py
```

This will initialize the graph, add edges, and perform BFS and DFS traversals. The graph will also be visualized.

## Features
- **Graph Representation**: Supports directed and undirected graphs.
- **Traversal Algorithms**: Implements BFS and DFS for graph traversal.
- **Dynamic Updates**: Allows adding and removing edges dynamically.
- **Graph Visualization**: Uses NetworkX and Matplotlib for visual graph representation.

## Contributions
Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
