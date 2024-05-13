class LinkedList:
    # What should happen when you create a LinkedList instance 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

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
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def find_middle(self):
        # Edge cases: empty list, one node in list, 
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        steps = 0
        while fast:
            fast = fast.next
            if steps % 2 == 0:
                if not fast:
                    return slow.value
                slow = slow.next
            steps += 1
        return slow.value
    
    def has_loop(self):
        # edge case: empty LL
        if not self.head:
            return False
    
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def find_kth_from_end(self, k):
        if self.head == None:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow
    
    def partition_list(self, x):
    # One of the keys here is that you are linking Nodes without make a list, 
    # however you then point the head of the list to the "chain" nodes you have linked
    # A dummy node is used at the beginning to start the high and low chains
    # At the end, You will be able to use dummy.next to access the "true" heads of the chains created from the while loop - a string of linked "prev" nodes!
        if self.head == None:
            return None
        temp = self.head
        prev1 = Node(0)
        prev2 = Node(0)

        dummy1 = prev1
        dummy2 = prev2

        while temp:
            if temp.value < x:
                prev1.next = temp
                prev1 = temp
            else:
                prev2.next = temp
                prev2 = temp
            temp = temp.next

        prev1.next = None
        prev2.next = None

        # end of first list to the "next" of dummy2, which is the proper head of the high list 
        prev1 = dummy2.next
        # set the head of the list to the "next" of dummy1, which is the proper head oof the high list  
        self.head = dummy1.next
        self.print_list() 
    
    def remove_duplicates(self):
        if not self.head:
            return True
        checker = set()
        prev = self.head
        current = self.head
        temp = self.head
        checker.add(current.value)
        
        while current:
            if current.value in checker:
                prev.next = current.next
                current.next = None
                current = prev.next
            else:
                checker.add(current.value)
                current = current.next
                prev = prev.next
        return True
    
    def bindary_to_decimal(self):
        temp = self.head
        running_total = 0
        count = 0
        while temp:
            running_total += temp.value * 2**(self.length - count - 1) 
            temp = temp.next
            count += 1
        return running_total
    
    def reverse_between(self, start, stop):
        if not self.head or self.length == 1:
            return None
        dummy_node = Node(0)
        # this points the dummy_node (eventually a bunch of liked nodes via .next attribute) into the actual LinkedList we want to modify 
        dummy_node.next = self.head
        # pointer to find the end of the section of the linked list that isn't reversed
        # you need this in order to point to the reversed section
        previous_node = dummy_node
        # this finds the node right before the section to reverse
        for _ in range(start):
            previous_node = previous_node.next
        # get the first node to be reversed, this will always be the last of the reversed list
        current = previous_node.next  
        for _ in range(stop - start):
            # initialize/get "the node to move", which is in front of the current node
            node_to_move = current.next
            # point the next of current to the "node to move's next", which is a next.next 
            current.next = node_to_move.next
            # point the node_to_move to what is after the previous node 
            node_to_move.next = previous_node.next
            # previous's next to the node to move so that on the next iteration, node to move points at the previously moved node  
            previous_node.next = node_to_move
        # set the head
        self.head = dummy_node.next



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
# linked_list.append(1)
# linked_list.append(0)
# linked_list.append(1)
linked_list.print_list()
print("========")
# print(linked_list.find_kth_from_end(6).value)
# print(linked_list.partition_list(7))
# print(linked_list.bindary_to_decimal())
linked_list.reverse_between(2,5)
linked_list.print_list()