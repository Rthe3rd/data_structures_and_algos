# Recursive Binary Search Tree

# What makes a valid Binary Search Tree
# 1. The value of a parent's left child is less than the parent
# 2. The value of a parent's right child is greater than the parent
# 3. Cannot have duplicates

# BST Constructor stays the same
# When creating a BST, you need a BST class and a Node class
# BST have a root node.  Here we create an "empty" root node so we can instantiate the class without a value
class BST:
    def __init__(self):
        self.root = None

    # Contains: 
    def contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_contains(self, current, value):
        if current == None:
            return False
        if current.value == value:
            return True
        if current.value > value:
            return self._r_contains(current.left, value)
        if current.value < value:
            return self._r_contains(current.right, value)

    # If the BST is empty, it will set the root accordingly
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        # Note you are not returning this value! A pointer to the node before the root (left or right) is returned to this method.  It is not needed so we do not return it
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        # Base case: if you called this method with a current_node == Node
        if current_node == None:
            # Creating a new node. Whichever case of insert called this final step will assign the "current.right/left" and thus the node is added to the BST
            return Node(value)
        if value < current_node.value:
            # Note you are not "traversing" (node = node.left) the tree here 
            # you are assigning the pointer of the current node to what is to the left of/less than it and calling the function with the next current_node 
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            # Note you are not "traversing" (node = node.right) the tree here 
            # you are assigning the pointer of the current node to what is to the right of/greater than it and calling the function with the next current_node 
            current_node.right = self.__r_insert(current_node.right, value)
        # 
        '''
        Return current node so that after the new node is assigned, or not assigned because the value was alread in the BST,
        every previous call that is to be "bubbled up" to will get assigned the !pointer! to the existing node => "continue pointing at that node"
        The final return will return will be to the initial __r_insert() that is found in the insert()
        This is the final "bubble up" which actually bubbles out of the current method and back into the r_insert method
        ''' 
        return current_node

    # Delete: Starting at the top of the tree, traverse the tree until you find the node/value to replace
    def delete(self, value):
        self.__delete_node(self.root, value)
        return
    
    def __delete_node(self, current_node, value):
        # Base case if you reach the end of the tree and never found the value
        if current_node == None:
            return None
        # traverse the tree by checking the current_node's value and the value to delete
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        # traverse the tree by checking the current_node's value and the value to delete
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # 4 conditions you need to code for within the else statement
            # 1. Deleting a leaf node
            # 2. Opening/no node on left and node on right
            # 3. Opening/no node on right and node on left
            # 4. Nodes on both left and right
        # If you reach here, that means that you have reached the bottom of the tree
        else:
            # 1. Deleting a leaf node
            if current_node.left == None and current_node.right == None:
                # Returning None will "bubble up" a *None* to the previous call to __delete_node => .left/.right = self.__r_delete(current_node.left/.right, value) 
                return None
            # 2. Opening/no node on left and node on right
            elif current_node.left == None:
                # Assigning the current_node to current_node.right will "bubble up" this node such that the previous function called will 
                    # assign the pointer to this node and "delete" whatever it was pointing at previously 
                current_node = current_node.right
            # 3. Opening/no node on right and node on left
                # Assigning the current_node to current_node.left will "bubble up" this node such that the previous function called will 
                    # assign the pointer to this node and "delete" whatever it was pointing at previously 
            elif current_node.right == None:
                current_node = current_node.left
            # 4. Nodes on both left and right
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            return current_node
    
    # Find the lowest value underneath a certain node
    def min_value(self, current_node):
        # check to see if left exists, if so, traverse to the left
        while current_node.left is not None:
            current_node = current_node.left
        # this will return the value of the lowest node
        return current_node.value

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)
    
    def __sorted_list_to_bst(self, nums, left, right):
        # Base case: This means you are either given an empty list of nums or left and right indices have "crossed over" and you've looked through all items in the array
        if left > right:
            return None
        # Integer division ensures that you are getting the "floor" when dividing, no decimals 
        middle_index = (right + left) // 2
        # Create the middle node/ current root/subtree root
        current_root = Node(nums[middle_index])
        # create the left subtree with current.left = 
        current_root.left = self.__sorted_list_to_bst(nums, left, middle_index - 1)
        current_root.right = self.__sorted_list_to_bst(nums, middle_index + 1, right)
        # return the root
        return current_root 


    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, current_root):
        # Base case: if the root given or you reach the bottom of the tree
        if current_root == None:
            return None
        # perform a swap on each side and recurse with the new "curent_root"
        temp = current_root.left
        current_root.left = self.__invert_tree(current_root.right)
        current_root.right = self.__invert_tree(temp)
        # return the node so everything bubbles up
        return current_root

    # Breadth-first search: search each level at a time
    def BFS(self):
        current_node = self.root
        # This list will hold the nodes themselves
        # We use nodes to check their left and right
        queue = []
        # Here we are appending just the node's value
        results = []
        # Append the full node into the queue BEFORE you run the while loop, so you don't start with an empty queue
        queue.append(current_node)
        while len(queue) > 0:
            # Note that .pop(0) is used to remove the first element in the list
            current_node = queue.pop(0)
            # Add the node's value to the list
            results.append(current_node.value)
            # IF the node has a child to the left, add the left child node to the list
            if current_node.left is not None:
                queue.append(current_node.left)
            # IF the node has a child to the right, add the right child node to the list
            if current_node.right is not None:
                # Add the node to the list
                queue.append(current_node.right)
        return results

    # Three types of Depth First Search or DFS
    # Only one function call on the call stack will run at a time.  
    # Once a new function call is added to the call stack, it will start running, putting the previous function on "hold" until it is finished  
    # ======================================== #
                # "VIST" VS "ADD"
    # ======================================== #
    # The out function isn't finished until the very first call on the call stack is removed, this is the last step
    # 1. Depth First Search: PreOrder
        # Function call starts with the root and bubbles down to left most node
        # Bubbles up to parent and down to right child if there is one
        # Once all children of a parent have been visted/added to results, 
        # This is the same process as the "subset" problem
    def dfs_pre_order(self):
        # results sits outside of the recursive function, so it is accessible and built with each recursive call
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            # If there is a left child, step left and put the left child "on the call stack"
            if current_node.left is not None:
                # You will only move past this point once there is not a left child.
                # At that point the node that was put on the call stack is removed and the next node on the call stack
                # which is its parent, moves on to the next conditional and function call
                traverse(current_node.left)
            # If there is a right child, step right and put the right child "on the call stack"
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    # Depth First Search: PostOrder
    # Left/right/write
    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
                # Appending happens once you've reached the right side
                results.append(current_node.value)
        traverse(self.root)
        return results

    # Depth First Search: InOrder.
    # Returns "results" with values in increasing order 
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            # Appending happens after you have reached the bottom on the left side
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    # Interview Questions
    # Validate BST: Given a BST, determine whether a BST is valid by class method
    # KEY: Traversing "In Order" should produce a list increasing in value
    def is_valid_bst(self):
        current_node = self.root
        if not current_node:
            return True
        results = self.dfs_in_order()
        for index in range(0, len(results)):
            if index == 0:
                continue
            elif results[index - 1] > results[index]:
                return False
        return True

    # Kth Smallest Node: Find kth smallest Node
    # KEYS
        # 1. Kth smallest is found by taking K and reducing it by 1 each time a value is checked (popped from the stack)
        # 2. Tree is traversed in-order using nested while loops
        # 3. The outermost loop has two conditions: when the stack is NOT empty or the "temp" node is not null
            # 3a. The first condition checks for when you've checked all nodes
                # The first condition will be false when you initially start and when you have checked all nodes
            # 3b. The second condition allows the while loop to begin with an empty stack
                # The second condition will be false when you have reached the left most node  
    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []    
        # start at the root of the tree      
        temp = self.root    
        
        while stack or temp:
            # traverse to the leftmost node
            while temp: 
                # add the node to the stack                
                stack.append(temp)      
                temp = temp.left
            # pop the last node added to the stack
            temp = stack.pop()           
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:                  
                return temp.value
            # move to the right child of the node
            temp = temp.right           
            
        # if k is greater than the number of nodes in the tree, return None
        return None  

    def kth_smallest_2(self, k):
        results = self.dfs_in_order()
        if k > len(results) or k <= 0:
            return None
        return results[k - 1]

# Node class has three attributes, value, left and right
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# my_tree = BST()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# my_tree.insert(4)

# print('ROOT:', my_tree.root.value)
# print('LEFT:', my_tree.root.left.value)
# print('RIGHT:', my_tree.root.right.right.value)

bst = BST()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest_2(7))
