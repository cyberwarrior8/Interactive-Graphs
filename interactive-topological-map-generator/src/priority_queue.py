class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(reverse=True)  # Prioridad más alta primero

    def get(self):
        return self.elements.pop()[1]  # Devuelve el elemento con la prioridad más alta

    def peek(self):
        return self.elements[-1][1] if self.elements else None  # Devuelve el elemento de mayor prioridad sin eliminarlo

    def size(self):
        return len(self.elements)  # Devuelve el número de elementos en la cola