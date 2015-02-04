__author__ = 'austin'

import unittest
from HW2.hw2_set import OurSet


class TestOurSet2(unittest.TestCase):

    def setUp(self):
        self.set1 = OurSet()
        self.set2 = OurSet()
        self.set3 = OurSet()

    def test_union(self):
        """Test union functionality."""
        self.set1.addList([1, 2, 3])
        self.set2.addList([3, 4, 5])
        self.set3.addList([1, 2, 3, 4, 5])
        self.set4 = self.set1.union(self.set2)
        for i in self.set4:
            self.assertTrue(i in self.set1 or i in self.set2, "Unioned sets not equal")

    def test_intersection(self):
        self.set1.addList([1, 2, 3])
        self.set2.addList([3, 4, 5])
        self.set3 = self.set1.intersection(self.set2)
        self.assertTrue(3 in self.set3, "Intersection test failed.")

if __name__ == '__main__':
    unittest.main()