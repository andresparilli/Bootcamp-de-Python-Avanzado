from typing import Iterator
# Elementos iterables
"""
Se crea el metdoo .__iter__() y este permite iterar sobre el objeto creado
"""


class MyIterable:
    def __init__(self, start: int, end: int) -> None:
        self.start: int = start
        self.end: int = end
        self.current: int = start  # Initialize the current value to 'start'

    def __iter__(self) -> Iterator[int]:
        return self  # This is fine

    def __next__(self) -> int:
        if self.current > self.end:
            raise StopIteration  # Stop iteration when 'current' exceeds 'end'

        value: int = self.current
        self.current += 1  # Increment the current value
        return value

# ----fin de codigo----
