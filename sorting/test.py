import unittest
import random

from bubble_sort import bubble_sort, shaker_sort
from selection_sort import selection_sort, double_selection_sort
from insertion_sort import insertion_sort, binary_insertion_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from shell_sort import shell_sort

class TestSorting(unittest.TestCase):
    def testSorting(self):
        """
        Test that it can sort arrays
        """
        algorithms = {
                "selection_sort": selection_sort,
                "double_selection_sort": double_selection_sort,
                "insertion_sort": insertion_sort,
                # "binary_insertion_sort": binary_insertion_sort,
                "bubble_sort": bubble_sort,
                "shaker_sort": shaker_sort,
                "quick_sort": quick_sort,
                "merge_sort": merge_sort,
                "shell_sort": shell_sort,
                }
        sorted_array = list(range(10))
        for alg_name in algorithms:
            random_array = list(range(10))
            random.shuffle(random_array)
            algorithms[alg_name](random_array)
            self.assertEqual(random_array, sorted_array, alg_name)
