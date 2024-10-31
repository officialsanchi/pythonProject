class Queue:
    def __init__(self, capacity):
        self._array = [None] * capacity
        self._size = 5
        self._capacity = capacity

    def get_size(self):
        return self._size

    def is_empty(self):
        return len(self._array) == 0

    def add(self, element):
        if len(self._array) >= self._size:
            raise IndexError('Queue is full')
        self._array.append(element)

    def count_elements(self):
        return len(self._array)

    def remove(self):
        number = self._array[0]
        self._array.pop(0)
        return number

    def element(self):
        return self._array[0]