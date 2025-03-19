import random
import tkinter as tk
from tkinter import messagebox
from graph import Graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from dynamic_updates import add_edge, remove_edge
from visualization import visualize_graph, animate_bfs, animate_dfs

def generate_random_graph(num_nodes, num_edges, directed=True, connected=True):
    if connected and num_edges < num_nodes - 1:
        raise ValueError("El número de aristas debe ser al menos num_nodes - 1 para conectar todos los nodos.")

    graph = Graph(directed=directed)
    nodes = [chr(i) for i in range(65, 65 + num_nodes)]  # Genera nodos con letras A, B, C, ...

    if connected:
        # Conectar todos los nodos para asegurar que el grafo sea conexo
        for i in range(num_nodes - 1):
            weight = random.randint(1, 10)
            graph.add_edge(nodes[i], nodes[i + 1], weight)

        edges = set((nodes[i], nodes[i + 1]) for i in range(num_nodes - 1))
    else:
        edges = set()

    while len(edges) < num_edges:
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            edge = (u, v) if directed else tuple(sorted((u, v)))
            if edge not in edges:
                edges.add(edge)
                weight = random.randint(1, 10)
                graph.add_edge(u, v, weight)

    return graph

def main():
    def generate_graph():
        try:
            num_nodes = int(entry_nodes.get())
            num_edges = int(entry_edges.get())
            directed = var_directed.get()
            connected = var_connected.get()

            if connected and num_edges < num_nodes - 1:
                messagebox.showerror("Error", "El número de aristas debe ser al menos num_nodes - 1 para conectar todos los nodos.")
                return

            global graph
            graph = generate_random_graph(num_nodes, num_edges, directed=directed, connected=connected)
            messagebox.showinfo("Éxito", "Grafo generado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def perform_bfs():
        if graph:
            bfs_result = bfs(graph, 'A')
            messagebox.showinfo("BFS Traversal", str(bfs_result))
        else:
            messagebox.showerror("Error", "Primero genere un grafo.")

    def perform_dfs():
        if graph:
            dfs_result = dfs(graph, 'A')
            messagebox.showinfo("DFS Traversal", str(dfs_result))
        else:
            messagebox.showerror("Error", "Primero genere un grafo.")

    def visualize():
        if graph:
            visualize_graph(graph)
        else:
            messagebox.showerror("Error", "Primero genere un grafo.")

    def animate_bfs_graph():
        if graph:
            animate_bfs(graph, 'A')
        else:
            messagebox.showerror("Error", "Primero genere un grafo.")

    def animate_dfs_graph():
        if graph:
            animate_dfs(graph, 'A')
        else:
            messagebox.showerror("Error", "Primero genere un grafo.")

    global graph
    graph = None

    root = tk.Tk()
    root.title("Generador de Grafos Topológicos")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")

    title_label = tk.Label(root, text="Generador de Grafos Topológicos", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=10)

    tk.Label(frame, text="Número de nodos:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
    entry_nodes = tk.Entry(frame)
    entry_nodes.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Número de aristas:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
    entry_edges = tk.Entry(frame)
    entry_edges.grid(row=1, column=1, padx=5, pady=5)

    var_directed = tk.BooleanVar()
    tk.Checkbutton(frame, text="Grafo dirigido", variable=var_directed, bg="#f0f0f0").grid(row=2, columnspan=2, pady=5)

    var_connected = tk.BooleanVar()
    tk.Checkbutton(frame, text="Grafo conexo", variable=var_connected, bg="#f0f0f0").grid(row=3, columnspan=2, pady=5)

    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Generar Grafo", command=generate_graph, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Realizar BFS", command=perform_bfs, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(button_frame, text="Realizar DFS", command=perform_dfs, bg="#FF9800", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Visualizar Grafo", command=visualize, bg="#9C27B0", fg="white", font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(button_frame, text="Animar BFS", command=animate_bfs_graph, bg="#E91E63", fg="white", font=("Helvetica", 12)).grid(row=2, columnspan=2, padx=10, pady=5)
    tk.Button(button_frame, text="Animar DFS", command=animate_dfs_graph, bg="#E91E63", fg="white", font=("Helvetica", 12)).grid(row=3, columnspan=2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()