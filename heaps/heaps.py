# Heaps

# In general, all child nodes are less than, or equal to, in value, to their parent nodes (directly above, not a different branch above)
# Complete: Heaps are complete trees that are filled left to right, meaning only the right most nodes can be left empty
# Height is how many levels that are present in the heap
# Duplicates: Duplicates are possible in a heap; i.e. child is equal to its parent

# Max vs. Min Heap
# Max Heap: max value at the top
# Min Heap: Min value at the top

# Heaps are not good for searching since the only requirement is that either the largest, or smallest, is at the top but thus is easily findable/removeable

# Storage: 
# In a list, with index starting at 0 or 1.  Math is easier with a 1-based index
# List is filled, top to bottom, left to right, with regards to the leaves on the tree.  A complete tree means that a list is filled with no gaps
# For a 1-based index, starting at index 1, the indices are as follow
    # left_index = 2 * parent_index 
    # right_index = 2 * parent_index + 1
    # parent_index = right_index // 2 (INTEGER DIVISION)

# For a 0-based index, starting at index 1, the indices are as follow
    # left_index = 2 * parent_index + 1
    # right_index = 2 * parent_index + 2
    # parent_index = (right_index - 1) // 2 (INTEGER DIVISION)
    # left_node, right_node = right_node, left_node

# Insert: Insert a vertex into the heap
    # Insertion starts at the first empty space; the furthest bottom, right spot and "bubbling" it up until it's in the correct position
    # Moving the vertex with a while loop; while parent is not NONE or while less than parent 

# For a 0-based index
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

    # INSERT FOR MAX HEAP
    def insert(self, value):
        # Insert the new value at the end of the list i.e. the very end of the heap
        self.heap.append(value)
        # Get the index of the last value
        current = len(self.heap) - 1
        # current > 0: If the current index was <= 0, that would mean subsequent swaps would result in out of bounds swaps
        # self.heap[current] > self.heap[self._parent(current)]: 
            # One of the few tenants of heaps, all children vertices are less than in value to their parent vertex
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            # Given two indices, one for current and one for parent, swap their positions in the tree
            self._swap(current, self._parent(current))
            # Adjust the current variable such that it points to the proper node, i.e. the parents index
            current = self._parent(current)

    # INSERT FOR MINHEAP
    # def insert(self, value):
    #     self.heap.append(value)
    #     current_index = len(self.heap) - 1
    #     while True:
    #         if current_index > 0 and self.heap[current_index] < self.heap[self._parent(current_index)]:
    #             self._swap(current_index, self._parent(current_index))
    #             current_index = self._parent(current_index)
    #         else:
    #             return

    # REMOVE NDOE AT GIVEN INDEX
    # First step is to make the heap complete
        # Take the bottom, right most vertex to the top node
    # From there, you need to "sink down" this top node to it's proper place
    # Cases: Empty heap, 1 item in the heap, 2 or more items in the heap 
    def remove(self, index):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        # Assign the variable max_value to the top most node (of the sub-heap given the index), which will be removed
        max_value = self.heap[index]
        # Assign the first value (top most position in the heap) to the bottom, right most vertex, returned by self.head.pop()  
        self.heap[index] = self.heap.pop()
        # Class method to adjust the values in the heap such that it follows the rules of a heap (all children vertices are less than in value to their parent vertex)
        self._sink_down(index)
        return max_value
    
    # SINK DOWN NODE/RAISE NEW TOP NODE
    def _sink_down(self, index):
        # Max index is the top-most index that needs be "sunk down"
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            # left_index < len(self.heap): if the left index is a valid array index
            # self.heap[left_index] > self.heap[max_index]: if the value below (on the left) is greater than the parents, change the max index  
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            # right_index < len(self.heap): if the right index is a valid array index 
            # self.heap[right_index] > self.heap[max_index]: if the value below (on the right) is greater than the parents, change the max index 
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            # max_index != index: Was the max_index adjusted; i.e. was the *value* of the node at the max_index there less than either of the values below it?
                # if so, swap the values and rename assign the index to the current max_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            # If the max_index didn't change, i.e. the value at the max_index is greater than the left and right children, 
                # no more sinking down is needed and exit the loop
            # Note that you only perform node swapping at the end IF the index max_index was changed.  
            # Node swapping is then done by calling the ._swap() helper method
            else:
                return

    # SINKDOWN FOR MINHEAP
    # def _sink_down(self, index):
    #     current_min = index
    #     while True:
    #         left_child = self._left_child(current_min)
    #         right_child = self._right_child(current_min)
    #         if left_child < len(self.heap) and self.heap[current_min] > self.heap[left_child]:
    #             current_min = left_child
    #         if right_child < len(self.heap) and self.heap[current_min] > self.heap[right_child]:
    #             current_min = right_child            
    #         if current_min != index:
    #             self._swap(current_min, index)
    #             current_min = index
    #         else:
    #             return

# Return the kth smallest value given an input array
def find_kth_smallest(input_array, k):
    max_heap = MaxHeap()
    count = 0
    if k >= len(input_array) or k <= 0:
        return 'Out of bounds!'
    for number in input_array:
        max_heap.insert(number)
        count += 1
        if len(max_heap.heap) > k:
            max_heap.remove(0)

    return max_heap.remove(0)

# Return the largest value "seen" given an input stream of integers
def stream_max(input_array):
    max_value_holder = []
    for number in input_array:
        if not max_value_holder:
            max_value_holder.append(number)
            max_heap = MaxHeap()
            max_heap.insert(number)
        else:
            max_heap.insert(number)
            max_value_holder.append(max_heap.heap[0])
    return max_value_holder

my_heap = MaxHeap()
my_heap.insert(4)
my_heap.insert(1)
my_heap.insert(2)
my_heap.insert(3)
my_heap.insert(5)
print(my_heap.heap)
# print(find_kth_smallest([12,10,8,6,4], -1))
# print(stream_max([1,42,3,4,5,6]))
