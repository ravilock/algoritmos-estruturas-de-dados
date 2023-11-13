import unittest

from hash_map import Map

class TestMap(unittest.TestCase):
    def test_map_len(self):
        """
        Test that it can return length
        """
        map = Map()
        map["oi"] = "oi"
        self.assertEqual(len(map), 1)

    def test_map_ocupation(self):
        """
        Test that it correctly calculates its ocupation
        """
        map = Map()
        map["oi"] = "oi"
        self.assertEqual(map.ocupation, 0.2)

    def test_map_setitem(self):
        """
        Test that it correctly sets its item and returns its value
        """
        map = Map()
        map["oi"] = "ola"
        self.assertEqual(map["oi"], "ola")
        map["oi"] = "olar"
        self.assertEqual(map["oi"], "olar")

    def test_map_delitem(self):
        map = Map()
        map["oi"] = "ola"
        self.assertEqual(map["oi"], "ola")
        del map["oi"]
        self.assertEqual(map["oi"], None)

    def test_map_iter(self):
        map = Map()
        map["key1"] = "value 1"
        map["key2"] = "value 2"
        keys = ["key1", "key2"]
        values = ["value 1", "value 2"]
        i = 0
        for key, value in map:
            self.assertEqual(key, keys[i])
            self.assertEqual(value, values[i])
            i += 1
