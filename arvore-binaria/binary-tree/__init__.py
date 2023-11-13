class Node:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def sucessor(self, node):
        if node.right is None:
            if node.parent is None:
                return None
            parent = node.parent
            if parent.left == node:
                return parent
        currentNode = node.right
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode


    def insert(self, value):
        if len(self) == 0:
            self.root = Node(value)
            self.length += 1
            return
        return self._insert(self.root, value)

    def _insert(self, node, value):
        if value > node.value:
            # Inserir pela direita
            if node.right is None:
                node.right = Node(value, parent = node)
                self.length += 1
                return
            return self._insert(node.right, value)
        else:
            # Inserir pela esquerda
            if node.left is None:
                node.left = Node(value, parent = node)
                self.length += 1
                return
            return self._insert(node.left, value)

    def list_in_order(self):
        result = []
        self._list_in_order(self.root.left, result)
        result.append(self.root.value)
        self._list_in_order(self.root.right, result)
        return result

    def _list_in_order(self, current, result):
        if current is None:
            return

        self._list_in_order(current.left, result)
        result.append(current.value)
        self._list_in_order(current.right, result)

    def remove(self, value):
        if self.root.value == value and len(self) == 1:
            self.root = None
            self.length = 0
            return
        return self._remove(self.root, value)

    def _remove(self, current, value):
        if current is None:
            return

        if value > current.value:
            return self._remove(current.right, value)
        elif value < current.value:
            return self._remove(current.left, value)

        if current.left is None and current.right is None: # Current não tem filhos
            parent = current.parent
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
            current.parent = None
            self.length -= 1
        elif current.right is not None and current.left is None: # Current tem apenas um filho (à direita)
            if current is self.root:
                self.root = current.right
                self.root.parent = None
            else:
                parent = current.parent
                if parent.left is current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                current.right.parent = parent
            self.length -= 1
        elif current.left is not None and current.right is None: # Current tem apenas um filho (à esquerda)
            if current is self.root:
                self.root = current.left
                self.root.parent = None
            else:
                parent = current.parent
                if parent.left is current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                current.left.parent = parent
            self.length -= 1
        else: # Current tem dois filhos
            sucessor = self.sucessor(current) # Sucessor é o maior da sub-ávore à esquerda do filho da direita do current
            if current.right is sucessor:
                if current is self.root:
                    current.left.parent = sucessor # Atualizar o filho à esquerda do root
                    sucessor.left = current.left
                    self.root = sucessor # Atualizar o root
                    sucessor.parent = None
                else:
                    parent = current.parent # Atualizar filho do parent
                    if parent.right is current:
                        parent.right = sucessor
                        sucessor.parent = parent
                    else:
                        parent.left = sucessor
                        sucessor.parent = parent

                    sucessor.left = current.left # Atualizar filho do sucessor
                    if current.left is not None:
                        current.left.parent = sucessor
            else:
                if current is self.root:
                    current.left.parent = sucessor
                    sucessor.left = current.left # Atualizar o filho à esquerda do root

                    sucessor.parent.left = sucessor.right # Atualizando o filho so sucessor
                    if sucessor.right is not None:
                        sucessor.right.parent = sucessor.parent

                    current.right.parent = sucessor
                    sucessor.right = current.right # Atualizar o filho à direita do root

                    self.root = sucessor # Atualizar o root
                    sucessor.parent = None
                else:
                    sucessor.parent.left = sucessor.right
                    if sucessor.right is not None:
                        sucessor.right.parent = sucessor.parent

                    parent = current.parent
                    if parent.right is current: # Atualizar filho do parent
                        parent.right = sucessor
                        sucessor.parent = parent
                    else:
                        parent.left = sucessor
                        sucessor.parent = parent

                    sucessor.left = current.left # Atualizar filho do sucessor
                    current.left.parent = sucessor
                    sucessor.right = current.right
                    current.right.parent = sucessor

                    return
            self.length -= 1

btree = BinaryTree()
btree.insert(10)
btree.insert(12)
btree.insert(13)
btree.insert(14)
btree.insert(8)
btree.insert(9)
btree.insert(6)
btree.insert(5)
btree.insert(7)
btree.insert(11)
btree.insert(12.5)
"""
    10
  8    12
 6  9 11 13
5 7   12.5 14
"""
print(btree.list_in_order(), btree.root, len(btree))
btree.remove(12)
print(btree.list_in_order(), btree.root, len(btree))
