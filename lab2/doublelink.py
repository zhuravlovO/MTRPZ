
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
    
    def get(self, index: int) -> str:
        if not (0 <= index < self.length()):
            raise IndexError("Index out of bounds for get operation")

        if index < self.length() // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length() - 1 - index):
                current_node = current_node.prev

        return current_node.data
    
    def deleteAll(self, element: str) -> None:
        if not isinstance(element, str):
             raise TypeError("Element to delete must be a character")

        current_node = self.head
        while current_node is not None:
            next_node_to_check = current_node.next
            if current_node.data == element:
                prev_node = current_node.prev
                next_node = current_node.next
                if prev_node is None and next_node is None:
                    self.head = None
                    self.tail = None
                elif prev_node is None:
                    self.head = next_node
                    if self.head: 
                        self.head.prev = None
                elif next_node is None:
                    self.tail = prev_node
                    if self.tail: 
                        self.tail.next = None
                else:
                    prev_node.next = next_node
                    next_node.prev = prev_node

                current_node.next = None
                current_node.prev = None
                self._size -= 1

            current_node = next_node_to_check
    
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0    

    def findFirst(self, element: str) -> int:
        if not isinstance(element, str):
             raise TypeError("Element to find must be a string (character)")

        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_node.data == element:
                return current_index
            current_node = current_node.next
            current_index += 1
        return -1

    def findLast(self, element: str) -> int:
        if not isinstance(element, str):
             raise TypeError("Element to find must be a string (character)")

        current_node = self.tail
        current_index = self.length() - 1
        while current_node is not None:
            if current_node.data == element:
                return current_index
            current_node = current_node.prev
            current_index -= 1
        return -1
    
    def clone(self) -> 'DoublyLinkedList':
        new_list = DoublyLinkedList()
        current_node = self.head
        while current_node is not None:
            new_list.append(current_node.data)
            current_node = current_node.next
        return new_list

    def extend(self, elements: 'DoublyLinkedList') -> None:
        if not isinstance(elements, DoublyLinkedList):
            raise TypeError("Can only extend with another DoublyLinkedList")

        current_node_in_other = elements.head
        while current_node_in_other is not None:
            self.append(current_node_in_other.data)
            current_node_in_other = current_node_in_other.next

    def reverse(self) -> None:
        if self.length() < 2:
            return

        current_node = self.head
        original_head = self.head
        original_tail = self.tail

        while current_node is not None:
            next_original = current_node.next
            temp_prev = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp_prev
            current_node = next_original

        self.head = original_tail
        self.tail = original_head
