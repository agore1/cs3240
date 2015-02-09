__author__ = 'ayg9fh'


class Graph:
    """Graph class including CRUD operations."""
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.dict = {}
        else:
            self.dict = graph_dict

    def get_adjlist(self, node):
        """List the adjacent nodes."""
        if node in self.dict:
            return self.dict[node]
        else:
            return None

    def is_adjacent(self, node1, node2):
        """Check for adjacency if nodes are present."""
        if node1 not in self.dict or node2 not in self.dict:
            return False
        if node1 in self.dict[node2] and node2 in self.dict[node1]:
            return True
        else:
            return False

    def num_nodes(self):
        """Return the number of nodes in the graph."""
        return len(self.dict)

    def __str__(self):
        """String representation of graph."""
        return self.dict.__str__()

    def __iter__(self):
        """Graph Iterator."""
        return self.dict.__iter__()

    def __contains__(self, node):
        """Graph membership operator."""
        return self.dict.__contains__(node)

    def __len__(self):
        """The number of nodes in the graph."""
        return len(self.dict)

    def add_node(self, node):
        """Add a node to the graph if not already present."""
        if node in self.dict:
            return False
        else:
            self.dict[node] = []
            return True

    def link_nodes(self, node1, node2):
        """Link two nodes in the graph. """
        if node1 not in self.dict or node2 not in self.dict:
            return False
        elif node1 in self.dict[node2] and node2 in self.dict[node1]:
            return False
        else:
            self.dict[node1].append(node2)
            self.dict[node2].append(node1)
            return True

    def unlink_nodes(self, node1, node2):
        """Unlink two nodes present in the graph."""
        if node1 not in self.dict or node2 not in self.dict:
            return False
        elif node1 in self.dict[node2] and node2 in self.dict[node1]:
            self.dict[node1].remove(node2)
            self.dict[node2].remove(node1)
            return True
        else:
            return False

    def del_node(self, node):
        if node not in self.dict:
            return False
        else:
            for i in self.dict:
                if node in self.dict[i]:
                    self.dict[i].remove(node)
            del self.dict[node]
            return True