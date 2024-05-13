# Heaps Practice

# Max/Min Heap class
    # Constructor
        # heap data structure?
        # Upon instantiation, create an empty list to fill, in proper order, the "nodes", of the heap
        # We do not need a node class since the typical attributes for nodes, various pointers, can be described purely with list methods
        # Since we do not have nodes, we use methods on the indices to get values we'd typically get from pointers
            # self.left => _left_child(self, index), self.parent = _parent(self, index)
    # Methods
        # _left_child(self, index): Given a parent node index, return the index of the left child
        # _rightt_child(self, index): Given a parent node index, return the index of the right child
        # _parent(self, index): Given a child node index, return the index of the parent
        # _swap(self, node_1, node_1): Given two nodes, swap them
        # insert(self, value): insert a value into the heap
        # remove(self, index): Given an index, remove the node there and ensure the max/min heap is sustained
            # _sinkdown(self, index): Given the index of the node being removed, ensure that the sub-heap below is kept in the proper form

# Challenge problems for Min/Max Heaps
# kth-smallest
# Largest/Smallest given an input stream

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # add value to the of the heap
        self.heap.append(value)
        # keep track of current index (the largest it can be) while you are moving the inserted value
        current_index = len(self.heap) - 1
        while True:
            # check if the current index is "inbounds" AND check if the inserted value is greater than it's parent
            if current_index > 0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
                self._swap(current_index, self._parent(current_index))
                current_index = self._parent(current_index)
            else:
                return

    def remove(self, index):
        # base cases: Empty Heap and one value in the MaxHeap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # The value to be removed is going to be removed
        value_to_remove = self.heap[index]

        # Put the last value in the heap in the spot where the removed index was
        # This will be moved down via the helper method 
        self.heap[index] = self.heap.pop()

        self._sink_down(index)
        return value_to_remove    

    # This method starts at the top of the "sub-heap"
    # Move last node up to the index being removed
    # Move the node down until it's in the correct place
        # Check left child: if the current value is less than the left child, change the current_index
    def _sink_down(self, index):
        current_index = index

        while current_index >= len(self.heap) - 1:
            if self.heap[current_index] < self.heap[self._left_child(current_index)]:
                current_index = self._left_child(current_index)
            if self.heap[current_index] < self.heap[self._right_child(current_index)]:
                current_index = self._right_child(current_index)
            if current_index != index:
                self._swap(current_index, index)
                index = current_index
            else:
                return

my_heap = MaxHeap()
my_heap.insert(1)
my_heap.insert(2)
my_heap.insert(3)
my_heap.insert(4)
my_heap.insert(5)
print(my_heap.heap)