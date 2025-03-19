import networkx as nx
import matplotlib.pyplot as plt
from algorithms.dikstra import dijkstra
from adjustText import adjust_text
from tkinter import messagebox
import matplotlib.animation as animation

def visualize_graph(graph):
    G = nx.DiGraph() if graph.is_directed() else nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G, k=2, iterations=100)  # Ajusta el parámetro k y el número de iteraciones

    def on_click(event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            for node, (nx, ny) in pos.items():
                if (x - nx)**2 + (y - ny)**2 < 0.01:  # Ajusta el radio de selección
                    selected_nodes.append(node)
                    if len(selected_nodes) == 2:
                        start, end = selected_nodes
                        cost, path = dijkstra(graph, start, end)
                        if cost == float("inf"):
                            messagebox.showerror("Error", "No hay una ruta posible entre estos dos nodos")
                        else:
                            messagebox.showinfo("Ruta más corta", f"Ruta más corta de {start} a {end}: {path} con costo {cost}")
                            highlight_path(G, pos, path)
                        selected_nodes.clear()
                    break

    def highlight_path(G, pos, path):
        edge_colors = ['black' if (u, v) not in zip(path, path[1:]) else 'red' for u, v in G.edges()]
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color=edge_colors)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.draw()

    selected_nodes = []
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', on_click)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Ajusta las posiciones de los nodos para evitar la superposición
    #texts = [plt.text(pos[node][0], pos[node][1], node, fontsize=10, ha='center', va='center') for node in G.nodes()]
    #adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black'))

    plt.show()

def animate_bfs(graph, start_node):
    G = nx.DiGraph() if graph.is_directed() else nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G, k=2, iterations=100)  # Ajusta el parámetro k y el número de iteraciones

    visited = set()
    queue = [start_node]
    traversal_order = []

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    def update(num):
        if queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                queue.extend(neighbor for neighbor in graph.get_neighbors(vertex) if neighbor not in visited)
                nx.draw_networkx_nodes(G, pos, nodelist=[vertex], node_color='red', ax=ax)
                plt.draw()
        elif len(visited) < len(G.nodes()):
            remaining_nodes = set(G.nodes()) - visited
            for node in remaining_nodes:
                nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='red', ax=ax)
            plt.draw()

    ani = animation.FuncAnimation(fig, update, frames=len(G.nodes()) + 10, repeat=False)
    plt.show()

def animate_dfs(graph, start_node):
    G = nx.DiGraph() if graph.is_directed() else nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G, k=2, iterations=100)  # Ajusta el parámetro k y el número de iteraciones

    visited = set()
    stack = [start_node]
    traversal_order = []

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    def update(num):
        if stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                stack.extend(neighbor for neighbor in graph.get_neighbors(vertex) if neighbor not in visited)
                nx.draw_networkx_nodes(G, pos, nodelist=[vertex], node_color='red', ax=ax)
                plt.draw()
        elif len(visited) < len(G.nodes()):
            remaining_nodes = set(G.nodes()) - visited
            for node in remaining_nodes:
                nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='red', ax=ax)
            plt.draw()

    ani = animation.FuncAnimation(fig, update, frames=len(G.nodes()) + 10, repeat=False)
    plt.show()