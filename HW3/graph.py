__author__ = 'ayg9fh'

class Graph:
    """Graph class including CRUD operations."""
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.dict = {}
        else:
            self.dict = graph_dict

    def get_adjlist(self, node):
        pass

    def is_adjacent(self, node1, node2):
        pass

    def num_nodes(self):
        pass



