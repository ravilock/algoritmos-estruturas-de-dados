class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self, *values):
        self.first = None
        self.last = None
        self.length = 0
        for value in values:
            self.append(value)

    def __len__(self):
        return self.length

    def __repr__(self):
        if len(self) == 0: return "[]"
        repr = "["
        current = self.first
        while current.next is not None:
             repr += str(current.value) + ", "
             current = current.next
        repr += str(current.value) + "]"
        return repr

    def __eq__(self, other):
        if not isinstance(other, List):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def append(self, value):
        if len(self) == 0:
            self.first = Node(value)
            self.last = self.first
            self.length += 1
            return
        self.last.next = Node(value)
        self.last = self.last.next
        self.length += 1

    def pop(self):
        if len(self) == 0:
            return
        elif len(self) == 1:
            returnValue = self.first.value
            self.first = None
            self.last = None
            self.length -= 1
            return returnValue
        previousNode = None
        currentNode = self.first
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        returnValue = currentNode.value
        previousNode.next = None
        self.last = previousNode
        self.length -= 1
        return returnValue

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._get_with_index(index)
        elif isinstance(index, slice):
            return self._get_with_slice(index)

    def _get_with_index(self, index):
        if index < 0: index += len(self)
        if index >= len(self) or index < 0:
            raise Exception("Index out of range")
        currentNode = self.first
        for _ in range(index):
            currentNode = currentNode.next
        return currentNode.value

    def _get_with_slice(self, index):
        start, stop, step = index.indices(len(self))
        result = List()

        if len(self) == 0:
            return result

        if step < 0:
            for i in range(start, stop, step):
                result.append(self[i])
        else:
            current = self.first
            for _ in range(start):
                current = current.next
            for _ in range(start, stop):
                result.append(current.value)
                for _ in range(step):
                    if current.next is None:
                        return result
                    current = current.next
        return result

    def __iter__(self):
        current = self.first
        for _ in range(len(self)):
            yield current.value
            current = current.next

    def __setitem__(self, index, value):
        if index < 0: index += len(self)
        if index >= len(self) or index < 0:
            raise Exception("Index out of range")
        currentNode = self.first
        for _ in range(index):
            currentNode = currentNode.next
        currentNode.value = value

    def __delitem__(self, index):
        if isinstance(index, int):
            self._del_with_index(index)
        elif isinstance(index, slice):
            self._del_with_slice(index)

    def _del_with_index(self, index):
        if index < 0: index += len(self)
        if index >= len(self) or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            if len(self) == 1:
                self.first = None
                self.last = None
                self.length -= 1
                return
            self.first = self.first.next
            if len(self) == 2:
                self.last = self.first
            self.length -= 1
            return
        previousNode = None
        currentNode = self.first
        for _ in range(index):
            previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = currentNode.next
        if currentNode == self.last:
            self.last = previousNode
        self.length -= 1

    def _del_with_slice(self, index):
        start, stop, step = index.indices(len(self))

        if len(self) == 0:
            return

        if step < 0:
            for i in range(start, stop, step):
                del self[i]
            return

        previousNode = None
        currentNode = self.first
        for _ in range(start):
            previousNode = currentNode
            currentNode = currentNode.next
        for _ in range(start, stop, step):
            if self.first == self.last:
                self.first = None
                self.last = None
                self.length = 0
                return
            
            if currentNode == self.last:
                self.last = previousNode
                previousNode.next = currentNode.next
                self.length -= 1
                return

            if currentNode == self.first:
                self.first = self.first.next
                self.length -= 1
                currentNode = self.first
                for _ in range(step - 1):
                    previousNode = currentNode
                    currentNode = currentNode.next if currentNode.next is not None else self.last
                continue

            previousNode.next = currentNode.next
            self.length -= 1
            for _ in range(step - 1):
                previousNode = currentNode
                currentNode = currentNode.next if currentNode.next is not None else self.last

    def count(self, value):
        count = 0
        for i in self:
            if i == value:
                count += 1
        return count

    def copy(self):
        return self[:]

    def reversed(self):
        return self[::-1]
