import unittest

from rqueue import Queue

class TestQueue(unittest.TestCase):
    def test_stack_pile(self):
        """
        Test that it can pile values
        """
        queue = Queue()
        self.assertEqual(len(queue), 0)
        queue.enqueue(1)
        self.assertEqual(len(queue), 1)
        queue.enqueue(2)
        self.assertEqual(len(queue), 2)

    def test_stack_unpile(self):
        """
        Test that it can unpile values
        """
        queue = Queue(1, 2, 3)
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(len(queue), 0)
