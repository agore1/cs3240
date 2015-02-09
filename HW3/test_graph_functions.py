__author__ = 'ayg9fh'

import unittest
from HW3.graph import Graph
from HW3.graph_functions import is_complete


class TestGraphFunctions(unittest.TestCase):
    """Tests for the Graph Functions."""

    def setUp(self):
        self.empty_graph = Graph()
        self.full_graph = Graph({'A': ['B'], 'B': ['A', 'C'], 'C': ['B']})
        self.complete_graph = Graph({'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['B', 'A']})

    def test_is_complete1_gf1(self):
        """test is_complete() on a graph with 0 nodes. GF1"""
        self.assertTrue(is_complete(self.empty_graph), "Test gf1 failed.")

    def test_is_complete2_gf2(self):
        """test is_complete() on an incomplete graph. GF2"""
        self.assertFalse(is_complete(self.full_graph), "Test gf2 failed.")

    def test_is_complete3_gf3(self):
        """test is_complete() on a complete graph. GF3"""
        self.assertTrue(is_complete(self.complete_graph), "Test gf3 failed.")
