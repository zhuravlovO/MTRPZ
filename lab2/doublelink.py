
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
        return self._size
    
    def append(self, element: str) -> None:
        if not isinstance(element, str):
            raise TypeError("Can only append characters to this list")
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1
