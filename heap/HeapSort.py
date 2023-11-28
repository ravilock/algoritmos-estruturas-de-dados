from random import shuffle
from heap import MaxHeap, MinHeap


class HeapSort:
    def __init__(self, v, sort='asc'):
        if sort == 'asc':
            self.__heap = MinHeap()
        else:
            self.__heap = MaxHeap()

        for valor in v:
            self.__heap.insert(valor)

        self.__ordenado = []
        while len(self.__heap) > 0:
            self.__ordenado.append(self.__heap.remove())

    @property
    def ordenado(self):
        return self.__ordenado

vetor = list(range(1, 50))
shuffle(vetor)

print(vetor)
hs = HeapSort(vetor)
print(hs.ordenado)
