
class BuiltinList:
    def __init__(self):
        self._data: list[str] = []

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return f"BuiltinList({self._data})"

    def length(self) -> int:
        return len(self._data)

    def append(self, element: str) -> None:
        if not isinstance(element, str):
            raise TypeError("Can only append characters to this list")
        self._data.append(element)

    def insert(self, element: str, index: int) -> None:
        if not isinstance(element, str):
            raise TypeError("Can only insert characters into this list")
        if not isinstance(index, int):
             raise TypeError("Index must be an integer")
        if not (0 <= index <= self.length()):
             raise IndexError("Index out of bounds for insert operation")
        self._data.insert(index, element)

    def delete(self, index: int) -> str:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not (0 <= index < self.length()):
            raise IndexError("Index out of bounds for delete operation")
        return self._data.pop(index)

    def get(self, index: int) -> str:
        if not isinstance(index, int):
             raise TypeError("Index must be an integer")
        if not (0 <= index < self.length()):
            raise IndexError("Index out of bounds for get operation")
        return self._data[index]

    def deleteAll(self, element: str) -> None:
        if not isinstance(element, str):
             raise TypeError("Element to delete must be a character")
        self._data = [item for item in self._data if item != element]

    def clear(self) -> None:
        self._data.clear()

    def findFirst(self, element: str) -> int:
        if not isinstance(element, str):
             raise TypeError("Element to find must be a string (character)")
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        if not isinstance(element, str):
             raise TypeError("Element to find must be a string (character)")
        try:
            reversed_data = self._data[::-1]
            reversed_index = reversed_data.index(element)
            original_length = len(self._data)
            return original_length - 1 - reversed_index
        except ValueError:
            return -1

    def clone(self) -> 'BuiltinList':
        new_list = BuiltinList()
        new_list._data = self._data.copy()
        return new_list

    def extend(self, elements: 'BuiltinList') -> None:
        if not isinstance(elements, BuiltinList):
             raise TypeError("Can only extend with another BuiltinList")
        self._data.extend(elements._data)

    def reverse(self) -> None:
        self._data.reverse()
