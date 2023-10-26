import unittest

from stack import Stack

class TestStack(unittest.TestCase):
    def test_stack_pile(self):
        """
        Test that it can pile values
        """
        stack = Stack()
        self.assertEqual(len(stack), 0)
        stack.pile(1)
        self.assertEqual(len(stack), 1)
        stack.pile(2)
        self.assertEqual(len(stack), 2)

    def test_stack_unpile(self):
        """
        Test that it can unpile values
        """
        stack = Stack(1, 2, 3)
        self.assertEqual(stack.unpile(), 3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.unpile(), 2)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.unpile(), 1)
        self.assertEqual(len(stack), 0)
