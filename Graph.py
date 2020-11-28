from typing import TypeVar, List, Dict, Tuple
T = TypeVar("T")

class Graph:
    """
    An undirected Graph with adjacency lists (dictionary)
    """

    def __init__(self):
        """
        Constructor
        """
        self._vertices: Dict[T, List[T]] = { }

    def add_edge(self, v: T, u: T) -> None:
        """
        Add an edge between v and u to the graph
        """
        if v not in self._vertices:
            self._vertices[v] = []
        if u not in self._vertices:
            self._vertices[u] = []

        self._vertices[v].append(u)
        self._vertices[u].append(v)

    def get_edges(self, v:T):
        """
        Return the list of edges for vertex v 
        """
        return self._vertices[v]
    
    def get_vertices(self) -> List[T]:
        """
        Return the list of the vertices in the graph
        """
        return self._vertices.keys()
    
    def edge_list(self) -> List[Tuple[T,T]]:
        """
        Return the list of edges in the graph as a list of tuples. 
        """
        l = []
        for v in self._vertices:
            for e in self._vertices[v]:
                l.append((v, e))
        return l
    
    def __str__(self):
        """
        Pretty print the adjacency lists of the graph.
        """
        r = ""
        for u in self.get_vertices():
            r += "{0} --> [".format(u)
            for v in self.get_edges(u):
                r+= "{0}, ".format(v)
            r += '{0}{0}]\n'.format(chr(0x8))
        return r