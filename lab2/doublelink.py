
class Node:
    def __init__(self, data: str):
        if not isinstance(data, str):
             raise TypeError("Node data must be a string (character)")
        self.data: str = data
        self.next: 'Node' | None = None
        self.prev: 'Node' | None = None

    def __repr__(self) -> str:
        #  відладкa
        return f"Node(data={repr(self.data)})"


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0 

    # Довжина списку
    def length(self) -> int:
        """Повертає поточну кількість елементів у списку."""
        return self._size

