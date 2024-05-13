# Graphs

# Graphs have vertices (nodes) and edges
# Some graphs have weighted edges: not all edges have the same cost to "travel" over
    # network routing protocols
    # maps with traffic
# Bi-directional edges: an edge goes both ways to and from a vertice
# Directional edges: an edge only goes one way from a vertice

# Adjaceny Matrices:
# Matrice that maps the relations between vertices
# If the edges are NOT weighted, 1's and 0's represent the connections between carious nodes
# If the edges are weighted, then the weights of the edges between two vertices go into the matrice
# Vertices are on the vertical axis
# Vertices on the horitontal axis represent the nodes in which those on the vertical can connect to 
# Bidirectional maps will have a symmetry across the 45 degree diagonal of 0's (where the vertice on the vertical axis == the vertice on the horizontal axis)

# Adjaceny List
# Dictionary with vertices as keys and the values are the connected vertices

# Big O for Adjacency Matrices vs. Adjacency Lists
# Space complexity: O(V^2) vs. O(V + E), where is the number of Vertices and E is the number of edges
# Time complexity for insertion of a vertex: O(V^2) vs. O(1)
    # You need to add an entire row and column when using a matrice vs simply adding an entry to a dictionary/hash
# Time complexity for insertion of an edge: O(1) vs. O(1)
    # Changing two values in the matrice vs. adding a value to a key in a dict/hash, it's the same
# Time complexity to remove an edge: O(1) vs. O(E)
    # Change two values in the matrice vs. looping through the number of edges held at a value E
# Time complexity to remove a vertex: O(V^s) vs. O(V + E)
    # Re-writting number of vertices vs. looping through the

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except:
                pass
            return True
        return False

    def remove_vertix(self, vertex):
        if vertex in self.adj_list.keys():
            for edge_vertrex in self.adj_list[vertex]:
                self.adj_list[edge_vertrex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_edge('A','B')
my_graph.add_edge('C','B')
my_graph.add_edge('C','A')
my_graph.print_graph()
my_graph.remove_vertix('A')
print('========')
my_graph.print_graph()