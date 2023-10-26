class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

class Stack:
    def __init__(self, *values):
        self.__first = None
        self.__last = None
        self.__length = 0
        for value in values:
            self.pile(value)

    def __len__(self):
        return self.__length

    def pile(self, value):
        if len(self) == 0:
            self.__first = Node(value)
            self.__last = self.__first
        else:
            self.__last.setNext(Node(value))
            self.__last = self.__last.next
        self.__length += 1

    def unpile(self):
        if len(self) == 0:
            raise IndexError("Cannot unpile empty stack")
        value = None

        if len(self) == 1:
            value = self.__first.value
            self.__first = None
            self.__last = None
        else:
            current = self.__first
            for _ in range(len(self) - 2): # move to the node before the last
                current = current.next
            value = current.next.value
            current.next = None
            self.__last = current
        self.__length -= 1
        return value
