class Stack:
    def __init__(self):
        self._items = []  # Usamos una lista para almacenar los elementos del stack

    def push(self, item):
        """Agrega un elemento al tope del stack."""
        self._items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento del tope del stack.
        Lanza una excepción si el stack está vacío."""
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Devuelve el elemento del tope del stack sin eliminarlo.
        Lanza una excepción si el stack está vacío."""
        if self.is_empty():
            raise Exception("Cannot peek into an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Verifica si el stack está vacío."""
        return len(self._items) == 0

    def size(self):
        """Devuelve el número de elementos en el stack."""
        return len(self._items)

