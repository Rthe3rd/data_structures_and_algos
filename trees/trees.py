# Trees

# Binary Trees: 
# Node based data structure that has attributes value, left and right pointer
# Full/Balanced Tree: Tree that has all nodes either pointing to two other nodes or no nodes
# Perfect Tree: Tree that has ever level full of nodes
# Complete Tree:  Tree that is being filled from the far left to to the right, does not need to be full/balanced or perfect
# A "child" node has a single parent
# Node without children is a leaf 

# Binary Search Tree - Basics
# Child nodes that are smaller in value than their parent are the "left" child
# Child nodes that are alarger in value than their parents are the "right" child
# Values are added to the tree by comparing the values to add to the the nodes in the tree, one by one, starting with the root node
    # If the node to add is smaller than the current node (root or otherwise), move to the left.  
    # If the node to add is larger than the current node (root or otherwise), move to the right

# Binary Search Tree - Big O
# Each level has 2^N - 1 nodes, where N is the number of levels in the tree
# For large n, the number is ~2^N
# To find, replace or add a node, it takes N steps
# So Big O for these processes are Olog(N) -> very efficient! 
    # technically, worst case scenario BST becomes a linked list and thus everything is O(n), aside from insert which is O(1)


class BST:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.root = new_node

        # OR: Allows you to create a BST without an initial value/root
    def __init__(self):
        self.root = None

    def insert(self, value):
        node_to_add = Node(value)
        if self.root is None:
            self.root = node_to_add
            return True
        temp = self.root
        while True:
            if node_to_add.value == temp.value:
                return False
            if node_to_add.value < temp.value:
                if temp.left is None:
                    temp.left = node_to_add
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node_to_add
                    return True
                temp = temp.right
        return True
    
    # Contains: Is the value given found
    def contains(self, value):
        if self.root is None:
            return False
        search = self.root
        while search is not None:
            if value == search.value:
                return True
            elif value > search.value:
                search = search.right
            else:
                search = search.left
        return False

    def print(self):
        return


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

my_bst = BST()
# my_bst.insert(10)
# my_bst.insert(5)
# my_bst.insert(2.5)
# my_bst.insert(15)
# my_bst.insert(6)
# my_bst.insert(20)
print(my_bst.contains(0))
# print(my_bst.root.left.right.value)
