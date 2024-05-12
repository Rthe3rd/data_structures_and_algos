# Doubly Linked Lists


# Node class: Node class for a DLL has the attributes "prev", "next" and the "value" itself
class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

# Doubly Linked List: When creating a doubly linked list we want to
    # 1. Create it's first node
    # 2. Assign that node to it's head AND tail
    # 3. Give attribute of length 
    # 4. Give the DLL a way to print all of it's nodes
class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        count = 0
        while temp:
            print(f'Index #{count}: {temp.value}')
            temp = temp.next
            count += 1

    # Append method: append() should add a Node to the DLL and change the DLL attribute of self.tail to the Node added
    # Edge cases: Empty DLL
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # You do not have to loop through all of the nodes since you have the DLL attribute of tail that points to the last node in the DLL  
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Pop method: pop() should remove the final node, and reassign the tail and return the popped value
    # Edge cases: Empty DLL, Single node DLL
    def pop(self):
        # Edge case #1: if you have an empty DLL
        # if self.head is None OR if self.length == 0
        if self.length == 0:
            return False
        temp = self.tail
        # if self.head == self.tail OR: if self.length == 1
        # Edge case #2: if you have 1 node in the DLL
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        # return the popped NODE
        return temp
    
    # Prepend method should add a node to the front of the DLL, reassign the head and return true
    # Edge cases: Empty DLL
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    # Pop First method should remove the first node of the DLL, reassign the head, decrement the length and return the node (value?) popped
    # Edge cases: Empty DLL, one node in the DLL
    def pop_first(self):
        if self.length == 0:
            return False
        temp = self.head    
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # Get method should return the node (value?) at the (zero based) index 
    # Edge cases: Index is either less than 0 or greater than the length 
        # Note that this does not explicitly check the length of the DLL
        # The second condition of the if statement checks for an empty DLL
    def get(self, index):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    # You can optimize the get method by iterating backward from the tail if index <= self.length/2
    # Edge cases: Same as before
    def get_opt(self, index):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    # Set method should change the value of the node at a given index
    # Edge cases: given index is "out of bounds"
    # Since we already have a get method, we can get the node at a given index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Insert method should replace the node at a particular index, not just change the value of that index
    # Edge cases: the given index is out of bounds, the index is the head/tail
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # elif index == self.length - 1:
        #     node_to_move = self.pop()
        #     self.append(value)
        #     self.append(node_to_move.value)
        else:
            # Instiate two pointers for the nodes before and after where the new node will be inserted
            node_to_add = Node(value) 
            prev = self.get(index - 1) # This is what they call "before" 
            node_to_move = prev.next # This is what they call "after".  This is O(1) vs. O(n) when using the get method
            # point the new node to the before and after nodes
            node_to_add.prev = prev
            node_to_add.next = node_to_move 
            # point the before and after nodes to the new node
            prev.next = node_to_add
            node_to_move.prev = node_to_add
            self.length += 1
            return True
    
    # Remove method should remove the node at the given index.  
    # Edge cases: Given index is out of bounds, DLL is 1 node, DLL is empty
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        else:
            # TWO WAYS
            prev = self.get(index - 1)
            node_to_remove = prev.next
            node_after_removed = node_to_remove.next
            
            prev.next = node_after_removed
            node_after_removed.prev = prev
            node_to_remove.prev = node_to_remove.after = None

            # temp = self.get(index)
            # temp.next.prev = temp.prev
            # temp.prev.next = temp.next
            # temp.next = None
            # temp.prev = None

            self.length -= 1
        return node_to_remove

    # CHALLENGE QUESTIONS

    # 1. Swap First and Last 
        # Swap the values of the first and last nodes
        # Edge cases: Empty and 1 Node DLL
    def swap_first_last(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True 
        head_value = self.head.value
        tail_value = self.tail.value
        self.head.value = tail_value
        self.tail.value = head_value

    # 2. Reverse
        # Change the direction of the pointers of each of the nodes
        # Change head and tail
        # Edge cases: empty DLL, 1 node DLL, 2 node DLL => the only real edge case is a 1 node DLL, which is handled by the while condition       
    def reverse(self):
        current_node = self.head
        while current_node:
            temp_next = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp_next
            current_node = temp_next

        temp_tail = self.tail
        self.tail = self.head
        self.head = temp_tail
        return True

    # 3. Is Palindrome
        # Edge case: empty list
    def is_palindrome(self):
        forward = self.head
        backward = self.tail
        while forward and backward:
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True
    
    # Swap Pairs: swap every pair, starting at the head
        # Edge cases: empty DLL, 1 Node, 2 Nodes(?)
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            second_node.prev = previous_node
            first_node.prev = second_node

            if first_node.next:
                first_node.next.prev = first_node

            self.head = first_node.next
            previous_node =  first_node
        self.head = dummy_node.next

        if self.head:
            self.head.prev = None


my_dll = DLL(1)
my_dll.append(5)
my_dll.append(11)
my_dll.append(2)
my_dll.append(30)
my_dll.print_list()
my_dll.reverse()
my_dll.print_list()
# my_dll.swap_pairs()
# my_dll.print_list()

