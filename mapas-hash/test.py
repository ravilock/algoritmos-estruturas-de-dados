import unittest

from hash_map import Map

class TestMap(unittest.TestCase):
    def test_map_len(self):
        """
        Test that it can return length
        """
        map = Map()
        self.assertEqual(len(map), 0)
