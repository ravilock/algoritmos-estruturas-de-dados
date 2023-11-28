class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class MinHeap:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.root is None:
            return ''

        result = ''
        queue = [self.root]
        while queue:

            current = queue.pop(0)

            result += f"{current} "

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    
    def insert(self, value):
        self.length += 1

        if self.root is None:
            self.root = Node(value)
            return
        node = self._insert(value)
        self._heapfy_up(node)

    def _insert(self, value, queue = None):
        if queue is None:
            queue = [self.root]

        current = queue.pop(0)

        if current.left is None:
            current.left = Node(value, current)
            return current.left
        if current.right is None:
            current.right = Node(value, current)
            return current.right

        queue.append(current.left)
        queue.append(current.right)
        return self._insert(value, queue)
    
    def _heapfy_up(self, node):
        if node.parent is None:
            return

        if node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            return self._heapfy_up(node.parent)

    def last(self):
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return current
    
    def remove(self):
        if self.root is None:
            return

        self.length -= 1
        result = self.root.value

        last = self.last()
        self.root.value = last.value

        if last is self.root:
            self.root = None
            return result

        if last.parent.left is last:
            last.parent.left = None
        else:
            last.parent.right = None
        self._heapfy_down(self.root)
        return result

    def _heapfy_down(self, node):
        if node is None:
            return

        smallest = node

        if node.left and node.left.value < smallest.value:
            smallest = node.left
        if node.right and node.right.value < smallest.value:
            smallest = node.right

        if smallest is not node:
            node.value, smallest.value = smallest.value, node.value
            self._heapfy_down(smallest)


class MaxHeap:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.root is None:
            return ''
        
        queue = [self.root]
        result = ''

        while queue:
            current = queue.pop(0)
            result += f'{current} '

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result


    def insert(self, value):
        self.length += 1

        if self.root is None:
            self.root = Node(value)
            return

        node = self._insert(value)
        self._heapfy_up(node)

    def _insert(self, value, queue = None):
        if queue is None:
            queue = [self.root]

        current = queue.pop(0)
        if current.left is None:
            current.left = Node(value, current)
            return current.left
        elif current.right is None:
            current.right = Node(value, current)
            return current.right

        queue.append(current.left)
        queue.append(current.right)
        return self._insert(value, queue)

    def _heapfy_up(self, node):
        if node.parent is None:
            return

        if node.value > node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            self._heapfy_up(node.parent)

    def last(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return current


    def remove(self):
        if self.root is None:
            return
        
        self.length -= 1
        result = self.root.value

        last = self.last()
        self.root.value = last.value

        if last is self.root:
            self.root = None
            return result

        if last.parent.left is last:
            last.parent.left = None
        else:
            last.parent.right = None
        self._heapfy_down(self.root)
        return result

    def _heapfy_down(self, node):
        if node is None:
            return

        biggest = node
        
        if node.right and node.right.value > biggest.value:
            biggest = node.right

        if node.left and node.left.value > biggest.value:
            biggest = node.left

        if biggest is not node:
            biggest.value, node.value = node.value, maior.value
            self._heapfy_down(biggest)

if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(5)
    heap.insert(8)
    heap.insert(9)
    heap.insert(7)
    heap.insert(6)
    heap.insert(4)
    heap.insert(20)

    print(heap)

    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
