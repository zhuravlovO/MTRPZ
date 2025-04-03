
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

    def insert(self, element: str, index: int) -> None:
        if not isinstance(element, str):
            raise TypeError("Can only insert characters into this list")

        if not (0 <= index <= self.length()):
             raise IndexError("Index out of bounds for insert operation")

        if index == self.length():
            self.append(element)
            return

        new_node = Node(element)

        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next

            prev_node = current_node.prev
            new_node.prev = prev_node
            new_node.next = current_node
            prev_node.next = new_node
            current_node.prev = new_node

        self._size += 1

    def delete(self, index: int) -> str:
        if not (0 <= index < self.length()):
            raise IndexError("Index out of bounds for delete operation")
        if self.length() == 1: 
            node_to_delete = self.head
            self.head = None
            self.tail = None
        elif index == 0: 
            node_to_delete = self.head
            self.head = node_to_delete.next
            self.head.prev = None
        elif index == self.length() - 1: 
            node_to_delete = self.tail
            self.tail = node_to_delete.prev
            self.tail.next = None
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            node_to_delete = current_node
            prev_node = node_to_delete.prev
            next_node = node_to_delete.next
            prev_node.next = next_node
            next_node.prev = prev_node

        data_to_return = node_to_delete.data
        self._size -= 1
        node_to_delete.next = None
        node_to_delete.prev = None
        return data_to_return