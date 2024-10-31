class Stack:

    def __init__(self, size):
        self._stack = []
        self.__element_number = 0
        self._size = size


    def get_size(self):
        return self._size


    def is_empty(self):
        return len(self._stack) == 0

    def push(self, element):
        if len(self._stack) >= self._size:
            raise IndexError("Stack is full")
        self._stack.append(element)
        self.__element_number += 1

    def pop(self):
        if self.__element_number == 0:
            raise IndexError("Stack is empty")
        number =  self._stack[self.__element_number -1]
        self._stack[self.__element_number - 1] = None
        self.__element_number -= 1
        return number

    def get_element_number(self):
        return self.__element_number

    def peek(self):
        return self._stack[self.__element_number-1]

    def search(self, element):
        number = self.__element_number
        for index in range(len(self._stack)):
            if element == self._stack[index]:
                return number
            number -= 1

        return -1