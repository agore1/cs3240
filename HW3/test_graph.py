__author__ = 'ayg9fh'

import unittest
from HW3.graph import Graph


class TestGraph(unittest.TestCase):
    """Tests for the Graph class."""

    def setUp(self):
        self.empty_graph = Graph()
        self.full_graph = Graph({'A': ['B'], 'B': ['A', 'C'], 'C': ['B']})
        # print(self.full_graph.dict)

    def test_get_adjlist1_g1(self):
        """Test get_adjlist on a node not in the graph. G1"""
        self.assertIsNone(self.full_graph.get_adjlist('D'), "Test g1 failed.")

    def test_get_adjlist2_g2(self):
        """Test get_adjlist on a node in the graph. G2"""
        # self.assertTrue(self.full_graph.get_adjlist('A'), "Test g2 failed.")
        print(self.full_graph.get_adjlist('B'))
        self.assertEqual(sorted(self.full_graph.get_adjlist('B')), ['A', 'C'])

    def test_is_adjacent1_g3(self):
        """Test is_adjacent on a node not in graph. G3"""
        self.assertFalse(self.full_graph.is_adjacent('D', 'B'), "Test g3 failed.")

    def test_is_adjacent2_g4(self):
        """Test is_adjacent on a node in graph. G4"""
        self.assertTrue(self.full_graph.is_adjacent('A', 'B'), "Test g4 failed.")

    def test_contains1_g5(self):
        """Test __contains__ on an item not in the graph. G5"""
        self.assertFalse(self.full_graph.__contains__('D'), "Test g5 failed.")

    def test_contains2_g6(self):
        """Test __contains__ on an item in the graph. G6"""
        self.assertTrue(self.full_graph.__contains__('B'), "Test g6 failed.")

    def test_len1_g7(self):
        """Test __len__ on an empty graph. G7"""
        self.assertEqual(self.empty_graph.__len__(), 0, "Test g7 failed.")

    def test_len2_g8(self):
        """Test __len__ on a graph of length 3. G8"""
        self.assertEqual(self.full_graph.__len__(), 3, "Test g8 failed.")

    def test_num_nodes1_g9(self):
        """Test num_nodes on an empty graph. G9"""
        self.assertEqual(self.empty_graph.num_nodes(), 0, "Test g9 failed.")

    def test_num_nodes2_g10(self):
        """Test num_nodes on a graph of length 3. G10"""
        self.assertEqual(self.full_graph.num_nodes(), 3, "Test g10 failed.")

    def test_add_node1_g11(self):
        """Test add_node on an empty graph. G11"""
        self.assertTrue(self.empty_graph.add_node('D'), "Test g11 failed.")

    def test_add_node2_g12(self):
        """Test add_node with a node already in the graph. G12"""
        self.assertFalse(self.full_graph.add_node('B'), "Test g12 failed.")
        self.assertTrue(self.full_graph.__contains__('B'), "Test g12 failed.")

    def test_link_nodes1_g13(self):
        """Test link_nodes with two unlinked nodes in the graph. G13"""
        self.assertTrue(self.full_graph.link_nodes('A', 'C'), "Test g13 failed.")
        self.assertTrue(self.full_graph.is_adjacent('A', 'C'), "Test g13 failed.")

    def test_link_nodes2_g14(self):
        """Test link_nodes with two already linked nodes in the graph. G14"""
        self.assertFalse(self.full_graph.link_nodes('A', 'B'), "Test g14 failed.")
        self.assertTrue(self.full_graph.is_adjacent('A', 'B'), "Test g14 failed.")

    def test_link_nodes3_g15(self):
        """Test link_nodes with one node not in graph. G15"""
        self.assertFalse(self.full_graph.link_nodes('A', 'D'), "Test g15 failed.")
        self.assertFalse(self.full_graph.__contains__('D'), "Test g15 failed.")

    def test_unlink_nodes1_g16(self):
        """Test unlink_nodes with two linked nodes in the graph.G16"""
        self.assertTrue(self.full_graph.unlink_nodes('A', 'B'), "Test g16 failed.")
        self.assertFalse(self.full_graph.is_adjacent('A', 'B'), "Test g16 failed.")

    def test_unlink_nodes2_g17(self):
        """Test unlink_nodes with two already unlinked nodes in the graph. G17"""
        self.assertFalse(self.full_graph.unlink_nodes('A', 'C'), "Test g17 failed.")
        self.assertFalse(self.full_graph.is_adjacent('A', 'C'), "Test g17 failed.")

    def test_unlink_nodes3_g18(self):
        """Test unlink_nodes with one node not in graph. G18"""
        self.assertFalse(self.full_graph.unlink_nodes('A', 'D'), "Test g18 failed.")
        self.assertFalse(self.full_graph.__contains__('D'), "Test g18 failed.")

    def test_del_node1_g19(self):
        """Test del_node on a node not present in the graph. G19"""
        self.assertFalse(self.full_graph.del_node('D'), "Test g19 failed.")

    def test_del_node2_g20(self):
        """Test del_node on a node present in the graph. G20"""
        self.assertTrue(self.full_graph.del_node('A'), "Test g20 failed.")
        self.assertFalse(self.full_graph.__contains__('A'), "Test g20 failed.")


if __name__ == '__main__':
    unittest.main()








