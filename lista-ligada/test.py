import unittest

from linked_list import List

class TestList(unittest.TestCase):
    def test_list_len(self):
        """
        Test that it can return length
        """
        lista = List(5, 6)
        self.assertEqual(len(lista), 2)

    def test_list_getitem(self):
        """
        Test that it can return item with index
        """
        lista = List(5, 6)
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[0], 5)
        self.assertEqual(lista[1], 6)

    def test_list_comparison(self):
        """
        Test that it can be compared
        """
        lista = List(5, 6)
        self.assertFalse(lista == [5, 6])
        self.assertFalse(lista == List())
        lista2 = List()
        self.assertFalse(lista == lista2)
        lista2.append(5)
        lista2.append(6)
        self.assertTrue(lista == lista2)

    def test_list_string_representation(self):
        """
        Test that it can be represented as string
        """
        lista = List()
        self.assertEqual(lista.__repr__(), "[]")
        self.assertEqual(lista.__repr__(), [].__repr__())
        lista.append(5)
        self.assertEqual(lista.__repr__(), "[5]")
        self.assertEqual(lista.__repr__(), [5].__repr__())
        lista.append(5)
        self.assertEqual(lista.__repr__(), "[5, 5]")
        self.assertEqual(lista.__repr__(), [5, 5].__repr__())

    def test_list_iterate(self):
        """
        Test that it can be iterated
        """
        lista = List(5, 6, 7)
        list_rep = [5, 6, 7]
        counter = 0
        for c in lista:
            self.assertEqual(c, list_rep[counter])
            counter += 1

        sum = 0
        for c in lista:
            sum += c
        self.assertEqual(sum, 5 + 6 + 7)

    def test_list_slicing(self):
        """
        Test that it can be sliced
        """
        # Slice empty list should return empty list
        lista = List()
        self.assertEqual(lista[:], lista)
        lista.append(5)
        lista.append(6)
        lista.append(7)
        lista.append(8)

        # Slicing a list from its length should return empty list
        self.assertEqual(lista[len(lista):], List())
        # Slicing list up to its first element should return empty lsit
        self.assertEqual(lista[:0], List())

        # items start through stop-1
        self.assertEqual(lista[1:3], List(6, 7))
        # item start through the rest of the array
        self.assertEqual(lista[0:], List(5, 6, 7, 8))
        self.assertEqual(lista[1:], List(6, 7, 8))
        self.assertEqual(lista[2:], List(7, 8))
        self.assertEqual(lista[3:], List(8))
        # item from the beginning through stop-1
        self.assertEqual(lista[:1], List(5))
        self.assertEqual(lista[:2], List(5, 6))
        self.assertEqual(lista[:3], List(5, 6, 7))
        self.assertEqual(lista[:4], List(5, 6, 7, 8))
        # a copy of the list
        self.assertEqual(lista[:], lista)
        # using the step
        self.assertEqual(lista[::2], List(5, 7))
        self.assertEqual(lista[1::2], List(6, 8))
        self.assertEqual(lista[::3], List(5, 8))

        # Negative Start:
        # last item in list
        self.assertEqual(lista[-1:], List(8))
        # last two items in list
        self.assertEqual(lista[-2:], List(7, 8))

        # # Negative Stop:
        # everything except the last item
        self.assertEqual(lista[:-1], List(5, 6, 7))
        # everything except the last two items
        self.assertEqual(lista[:-2], List(5, 6))
        # everything except the last three items
        self.assertEqual(lista[:-3], List(5))

        # Negative Step:
        # all items in list, reversed
        self.assertEqual(lista[::-1], List(8, 7, 6, 5))
        # the first two items, reversed
        self.assertEqual(lista[1::-1], List(6, 5))
        # the last two items, reversed
        self.assertEqual(lista[:-3:-1], List(8, 7))
        # everything except the last two items, reversed
        self.assertEqual(lista[-3::-1], List(6, 5))

    def test_list_setitem(self):
        """
        Test that it can set item
        """
        lista = List()
        lista.append(5)
        lista.append(6)
        lista.append(7)
        lista[1] = 8
        self.assertEqual(lista[0], 5)
        self.assertEqual(lista[1], 8)
        self.assertEqual(lista[2], 7)
        self.assertNotEqual(lista[1], 6)

    def test_list_delitem(self):
        """
        Test that it can delete an item
        """
        lista = List(5)
        del lista[0]
        self.assertEqual(lista, List())

        lista = List(5, 6)
        del lista[0]
        self.assertEqual(lista, List(6))

        lista = List(5, 6)
        del lista[1]
        self.assertEqual(lista, List(5))
        del lista[0]
        self.assertEqual(lista, List())

        lista = List(5, 6, 7)
        del lista[1]
        self.assertEqual(lista, List(5, 7))
        del lista[1]
        self.assertEqual(lista, List(5))
        del lista[0]
        self.assertEqual(lista, List())

    def test_list_delitem_slicing(self):
        """
        Test that it can delete an item using slices
        """
        # Del Slicing a list from its start to above its length
        lista = List(5)
        del lista[0:2]
        self.assertEqual(lista, List())
        # Del Slicing from its start to its stop-1
        lista = List(1, 2, 3, 4, 5)
        del lista[0:3]
        self.assertEqual(lista, List(4, 5))
        # Del slicing from start to end of list
        lista = List(1, 2, 3, 4, 5)
        del lista[0:]
        self.assertEqual(lista, List())
        # Del slicing from index 1 to end
        lista = List(1, 2, 3)
        del lista[1:]
        self.assertEqual(lista, List(1))
        # Del slicing from index 2 to end
        lista = List(1, 2, 3)
        del lista[2:]
        self.assertEqual(lista, List(1, 2))
        # Del slicing from index 3 to end
        lista = List(1, 2, 3)
        del lista[3:]
        self.assertEqual(lista, List(1, 2, 3))
        # Del slicing the whole list
        lista = List(1, 2, 3, 4, 5)
        del lista[:]
        self.assertEqual(lista, List())
        # Using the step
        lista = List(1, 2, 3, 4)
        del lista[::2]
        self.assertEqual(lista, List(2, 4))
        lista = List(1, 2, 3, 4)
        del lista[1::2]
        self.assertEqual(lista, List(1, 3))
        lista = List(1, 2, 3, 4)
        del lista[::3]
        self.assertEqual(lista, List(2, 3))
        
        # Negative Start
        # Del slicing last element of list
        lista = List(1, 2, 3, 4)
        del lista[-1:]
        self.assertEqual(lista, List(1, 2, 3))
        # Del slicing last two elements of list
        del lista[-2:]
        self.assertEqual(lista, List(1))

        # Negative Stop
        # Del slicing everything except the last item
        lista = List(1, 2, 3, 4, 5)
        del lista[:-1]
        self.assertEqual(lista, List(5))
        # Del slicing everything except the two last item
        lista = List(1, 2, 3, 4, 5)
        del lista[:-2]
        self.assertEqual(lista, List(4, 5))
        # Del slicing everything except the three last item
        lista = List(1, 2, 3, 4, 5)
        del lista[:-3]
        self.assertEqual(lista, List(3, 4, 5))

        # Negative Step:
        # Del slicing the first two items, reversed
        lista = List(1, 2, 3, 4, 5)
        del lista[1::-1]
        self.assertEqual(lista, List(3, 4, 5))
        # Del slicing the last two items, reversed
        lista = List(1, 2, 3, 4, 5)
        del lista[:-3:-1]
        self.assertEqual(lista, List(1, 2, 3))
        lista = List(1, 2, 3, 4, 5)
        # everything except the last two items, reversed
        del lista[-3::-1]
        self.assertEqual(lista, List(4, 5))


    def test_list_append(self):
        """
        Test that it can append values
        """
        lista = List()
        lista.append(5)
        self.assertEqual(lista[0], 5)
        self.assertEqual(len(lista), 1)
        lista.append(6)
        self.assertEqual(lista[1], 6)
        self.assertEqual(len(lista), 2)

    def test_list_pop(self):
        """
        Test that it can pop values
        """
        lista = List(5, 6)
        self.assertEqual(lista[0], 5)
        self.assertEqual(lista[1], 6)
        self.assertEqual(len(lista), 2)
        value = lista.pop()
        self.assertEqual(value, 6)
        self.assertEqual(len(lista), 1)

    def test_list_count(self):
        """
        Test that it can count how many times it holds an value
        """
        lista = List(1, 2, 3, 4, 5, 5, 6)
        self.assertEqual(lista.count(1), 1)
        self.assertEqual(lista.count(5), 2)
        self.assertEqual(lista.count(6), 1)
        self.assertEqual(lista.count(7), 0)

    def test_list_copy(self):
        """
        Test that it can create copies of itself
        """
        lista = List(4, 3, 2, 1)
        lista2 = lista.copy()
        self.assertEqual(lista, lista2)
        lista2[1] = 100
        self.assertNotEqual(lista, lista2)

    def test_list_reversed(self):
        """
        Test that it can create a reversed copy of itself
        """
        lista = List(4, 3, 2, 1)
        lista2 = lista.reversed()
        self.assertEqual(lista2, List(1, 2, 3, 4))

if __name__ == '__main__':
    unittest.main()
