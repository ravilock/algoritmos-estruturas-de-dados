class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

class List:
    def __init__(self, *values):
        self.__first = None
        self.__last = None
        self.__length = 0
        for value in values:
            self.append(value)

    def append(self, value):
        if (self.__length == 0):
            self.__first = Node(value)
            self.__last = self.__first
        else:
            self.__last.setNext(Node(value))
            self.__last = self.__last.next
        self.__length += 1

    def pop(self):
        value = None
        if self.__length == 0:
            raise IndexError("Pop from empty list")
        elif self.__length == 1:
            value = self.__first.value
            self.__first = None
        else:
            currentNode = self.__first
            for _ in range(self.__length - 2):
                currentNode = currentNode.next
            value = currentNode.next.value
            currentNode.next = None
        self.__length -= 1
        return value

    def count(self, value):
        count = 0
        for element in self:
            if value == element:
                count += 1
        return count

    def copy(self):
        return self[:]

    def reversed(self):
        return self[::-1]
    
    def remover(self, value):
        print("Imprementá")

    def __len__(self):
        return self.__length

    def __eq__(self, __value):
        if not isinstance(__value, List):
            return False
        if len(self) != len(__value):
            return False

        currentSelf = self.__first
        currentValue = __value.__first

        for _ in range(len(self)):
            if currentSelf.value != currentValue.value:
                return False
            currentSelf = currentSelf.next
            currentValue = currentValue.next

        return True

    def __iter__(self):
        currentNode = self.__first
        while currentNode is not None:
            yield currentNode.value
            currentNode = currentNode.next

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._slice(index)
        else:
            return self._getItem(index)

    def _process_slice(self, index):
        step = index.step if index.step is not None else 1
        if step > 0:
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else len(self)
            if stop < 0:
                stop += len(self)
        else:
            start = index.start if index.start is not None else len(self) - 1
            stop = index.stop if index.stop is not None else -1
            if stop < -1:
                stop += len(self)

        if start < 0:
            start += len(self)
        return start, stop, step


    def _slice(self, index):
        start, stop, step = self._process_slice(index)

        # print("1-", start, stop, step)
        # print("2-", index.indices(len(self))) # Use this function to debug and test
        values = List()
        for i in range(start, stop, step):
            values.append(self[i])
        return values
    
    def _getItem(self, index):
        if index < 0:
            index += len(self)
        if index < 0 or index >= self.__length:
            raise IndexError("List index out of range")

        currentNode = self.__first
        for _ in range(index):
            currentNode = currentNode.next
        return currentNode.value

    def __setitem__(self, position, value):
        if position < 0:
            position += len(self)

        if position < 0 or position >= len(self):
            raise IndexError("List index out of range")
        
        atual = self.__first
        for _ in range(position):
            atual = atual.next
        atual.value = value

    # falta implementar deleção por fatia
    def __delitem__(self, position):
        if position < 0:
            position += len(self)

        if position < 0 or position >= len(self):
            raise IndexError("List index out of range")

        self.__length -= 1
        
        if self.__first == self.__last:
            self.__first == None
            self.__last == None
            return
        
        if position == 0:
            self.__first = self.__first.next
            return

        atual = self.__first
        for _ in range(position - 1):
            atual = atual.next

        if position == self.__length:
            atual.next = None
            self.__last = atual
        else:
            deletable = atual.next
            atual.next = deletable.next
            deletable.next = None

    def __repr__(self) -> str:
        if self.__length == 0:
            return "[]"

        printables = "["
        currentNode = self.__first
        while currentNode.next is not None:
            printables += f"{currentNode.value}, " 
            currentNode = currentNode.next
        printables += f"{currentNode.value}]"
        return printables

