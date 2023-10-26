class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

class Queue:
    def __init__(self, *values):
        self.__first = None
        self.__last = None
        self.__length = 0
        for value in values:
            self.enqueue(value)

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        if len(self) == 0:
            self.__first = Node(value)
            self.__last = self.__first
        else:
            self.__last.setNext(Node(value))
            self.__last = self.__last.next
        self.__length += 1

    def dequeue(self):
        if len(self) == 0:
            raise IndexError("Cannot unpile empty stack")

        value = self.__first.value
        self.__first = self.__first.next
        self.__length -= 1
        return value
