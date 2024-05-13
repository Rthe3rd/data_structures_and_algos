# Stacks
# LIFO data structure - Last thing in is the first thing to be taken out
# In other words, any structure that adds and removes items from the same end
# O(n) for adding and removing from the stack (push/pop)
# The simplest would be to implement a stack with a list data structure in python, array in 
# You can also create a stack with a singly linked list 
    # the tail is the first node added to the stack and it is at the "bottom" of the stack.  It points to None.
    # the most recent node added to the stack is at the "top" of the stack and will be called "top".



class Stack:
    # When initializing a stack 
        # 1. Create a the first "stack"
        # 2. Define attributes: self.top, self.height 
    def __init__(self, value):
        new_node = StackNode(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    # Push: Add node to the top of the stack, reassign top attribute
        # Edge case: empty stack
    def push(self, value):
        stack_node_to_add = StackNode(value)
        if self.height == 0:
            self.top = stack_node_to_add
        else:
            stack_node_to_add.next = self.top
            self.top = stack_node_to_add
        self.height += 1

    def pop(self):
        if self.height == 0:
            return False
        temp = self.top
        next_top = self.top.next
        temp.next = None
        self.top = next_top
        self.height -= 1
        return temp
    
def is_balanced_parentheses(string_to_check):
    if len(string_to_check) == 0:
        return True
    my_stack = Stack(0)
    for index in range(len(string_to_check)):
        if string_to_check[index] == '(':
            my_stack.push(string_to_check[index])
        else:
            my_stack.pop()
    if my_stack.height != 1:
        return False
    return True

def is_balanced_parentheses_2(string_to_check):
    my_stack = []
    for p in string_to_check:
        if p == "(":
            my_stack.append(p)
        elif p == ")":
            if len(my_stack) == 0 or my_stack.pop() != '(':
                return False
    if len(my_stack) == 0:
        return True
    return False

def reverse_string(string_to_reverse):
    # my_stack = Stack()
    my_stack = []
    for letter in string_to_reverse:
        my_stack.append(letter)
    string_to_return = ''
    while len(my_stack) != 0:
        string_to_return += my_stack.pop()
    return string_to_return

# sorts an unordered stack to an ascending stack
# def sort_stack(input_stack):
#     my_stack = Stack()
#     while not input_stack.is_empty():
#         temp = input_stack.pop()
#         while not my_stack.is_empty() and my_stack.peek() > temp:
#             input_stack.push(my_stack.pop())
#         my_stack.push(temp)
#     while not my_stack.is_empty():
#         input_stack.push(my_stack.pop())
#     return input_stack

class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


print(reverse_string('abcdefg'))

# my_stack = Stack(4)
# my_stack.push(5)
# my_stack.push(6)
# my_stack.push(7)
# my_stack.push(8)
# my_stack.pop()
# my_stack.print_stack()

class Queue:
    def __init__(self, value):
        new_node = QueueNode(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
        return True

    def enqueue(self, value):
        queue_node_to_add = QueueNode(value)
        if self.length == 0:
            self.first = queue_node_to_add
            self.last = queue_node_to_add
        else:
            self.last.next = queue_node_to_add 
            self.last = queue_node_to_add
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        removed_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            removed_node.next = None
        self.length -= 1
        return removed_node


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None 

# my_queue = Queue(1)
# my_queue = Queue(5)
# my_queue.enqueue(15)
# my_queue.enqueue(20)
# my_queue.enqueue(25)
# my_queue.dequeue()

# my_queue.print_queue()
        
