__author__ = 'horton'

import unittest
from queue import Queue

class TestQueue1(unittest.TestCase):

    def setUp(self):
        self.emptyQ = Queue()
        self.q1 = Queue([1, 2, 3])

    def test_remove1(self):
        """Q4: test calling remove on queue of size >1"""
        item = self.q1.remove()
        self.assertEqual(item, 1, "did not return 1st item in queue")
        self.assertEqual(2, len(self.q1), "queue should have 2 items")


if __name__ == '__main__':
    unittest.main()
