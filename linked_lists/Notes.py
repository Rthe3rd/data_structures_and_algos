# Linked Lists

head = {
    'value': 11,
    'next': {
        'value':3,
        'next': {
            'value': 44,
            'next': {
                # ......
            }
        }
    }
}

# Setting up the Linked List Class
    # Constructor: What should happen everytime a LinkedList is created?
    # appened - creates a new node at the end of the list
    # prepend - creates a new node at the start of the list
    # insert - creates a new node where specified
        # Since most methods will create a node, we need a class to create nodes; "Nodes"

# Setting up the Node Class
# What should a method return? If it's going to be used by other methods, you should be meaningful in what is returned
    # return Node? True? False?

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Print all nodes
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Add a node to the end of the list
# This is done in O(1) time - no loops needed
    def append(self, value):
        node_to_add = Node(value)
        if self.head is None:
            self.head = node_to_add
            self.tail = node_to_add
        else:
            self.tail.next = node_to_add
            self.tail = node_to_add
        self.length += 1
        return True
        # get tail to point to new node
        # point new node to none
    
    def pop(self):
        # Two edge cases: empty list and single list. One is handled up front, the other is cleverly handled at the end by checking the resulting length
        # EDGE CASE 1: The LL had no nodes
        if self.head is None:
            return 'Empty LL, nothing to pop!'
        temp = self.head
        pre = self.head
            # use pre and temp variables to keep track of what you are going to rename to tail and what you will pop + return
        while(temp.next): #  OR while temp.next is not None
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # EDGE CASE 2: The LL (previously) had 1 node
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head == new_node
            self.tail == new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return 'Empty - nothing to pop'
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index >= self.length or index < 0:
            return False
        count = 0
        current_node = self.head
        while count < index:
            current_node = current_node.next
            count += 1
        return current_node
    
    def set_value(self, index, value):
        # since we are "reaplceing" a node, and we have the "get" method, the code is simple 
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert_value(self, index, value):
        if index > self.length or index < 0:
            return False
        # Don't forget to return! That way you don't have the program continuing to run after you've inserted the node via class method.
        # What should you return?
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # ====== Explicit loop version ====== #
        # current = self.head
        # node_to_insert = Node(value)
        # for i in range(index):
        #     current = current.next
        # temp = current.next
        # current.next = node_to_insert
        # node_to_insert.next = temp'

        # ====== Implicit loop version via class method get() ====== #
        # OR without a for loop: Instead of "walking"/looping through the list to get the node before hand, 
        # make use of the get() method that already does that for you!
        node_to_insert = Node(value)
        temp = self.get(index - 1)
        node_to_insert.next = temp.next
        temp.next = node_to_insert
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            # opposite returning a Node
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        node_to_remove = temp.next
        # Using node_to_remove self.get() is slower since it requires stepping/looping through the linked list
        # node_to_remove = self.get(index)
        temp = self.get(index - 1)
        temp.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove

    def reverse(self):
        if self.length <= 1:
            return self
        # this will step through until you are at the last "index"
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


my_linked_list = LinkedList(4)
my_linked_list.append(111)
my_linked_list.append(400)
my_linked_list.print_list()
print('++++')
my_linked_list.reverse()
my_linked_list.print_list()