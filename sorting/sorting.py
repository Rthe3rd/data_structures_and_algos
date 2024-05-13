# Sorting

# KEEP IN MIND THE DIFFERENCE BETWEEN POINTERS THAT STAY WITH THE LOOP VS. THOSE THAT ARE RE-ASSIGNED DUE TO COMPARISIONS
    # pointers help you move through a list (data structure) as well as allow you to compare values.
    # Which pointers are for which purpose?  Which pointer should change "naturally", i.e. due to an incrementing/decrementing for-loop or natural while loop
        # vs. which pointer should change because of a comparision?  One is "natural" one is "dynamic"

# Space complexity
# All three of these sort the list in place. That means that they do not create additional copies of the list. That means it the space complexity is O(1)

# Time complexity
# Each of these three sorting algorithms have a loop within a loop so they are O(n^2).
# Only Insertion Sort is O(n) when you start with sorted (or almost sorted) data.

# Bubble sort
# Big O: O(n^2)
def bubble_sort(my_list):
    # The outer loop is used to determing the size of the inner loop
    # It is *NOT* used to indentify indices/values
    # Boundary condition is such that you do not sort when i == 0, everything will be sorted by then 
    for i in range(len(my_list) - 1, 0, -1):
        # Loop through all the values in the list up until, not including, the value at i
        # Each time that this loop is completed, the i-th max value is sorted
        # Start at j = 0 and end at index i - 1
        for j in range(i):
            # If the value at j is greater than what is ahead of it at j + 1, swap the values
            if my_list[j] > my_list[j+1]:
                # perform temp swap
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

# Selection sort
# The outer loop determines which values the inner loop will compare as the inner loop's range is defined by i => for j in range(i + 1, len(list))
# The index of the minimum value is found via the inner loop.  The inner loop moves forward from index = i + 1 to the end of the list, 
    # comparing the value at the current "min_index" to subsequent values in the list.  If a new, lower value is found, the min_index 
    # variable is reassigned and looping continues until the end of the list.
    # If the min_index changed during the inner loop, the value at the min_index is swapped with the value at the outer loop's variable i
# Selection sort works opposite to bubble sort. With bubble sort, the largest value is found first and moved to the last index.  
    # The remaining values are found in descending order and moved/bubbled to the back of the list.  Selection sort finds the smallest value 
    # first and moves it to the first position.  Values are moved in ascending order to the front until the second largest value is put second to last.   
def selection_sort(input_list):
    # Boundary condition is up until the second to last value
    for i in range(len(input_list) - 1):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        if min_index != i:
            temp = input_list[i]
            input_list[i] = input_list[min_index]
            input_list[min_index] = temp
    return input_list

# Insertion sort
# Big O: O(n^2) worst case, ~O(n) when the list is nearly/completely sorted 
# Starting at the second value, continiously compare the value to what is before it.  If it is less than the value before it, perform a swap
# Continue this swapping until either the index reaches 0 OR the current value is greater than the one before.  Once this happens, move to the next value in the list 
def insertion_sort(array_to_sort):
    # start at index of 1, the second item in the list
    for i in range(1, len(array_to_sort)):
        # temp is used to compare values
        temp = array_to_sort[i]
        # second pointer determines which values to compare to temp
        j = i - 1
        # While the following is true, peform a swap and move the second pointer in which to compare backwards 1
        while temp < array_to_sort[j] and j > -1:
            array_to_sort[j+1] = array_to_sort[j]
            array_to_sort[j] = temp
            j -= 1
    return array_to_sort

# Merge sort will be called recursively
# Big O: The breaking apart of lists is O(log n) time complexity.  8 items takes 3 steps to split into 8 groups of 1 
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    # Mid point is used to split the list in half. Int makes sure to round
    mid_index = int(len(my_list)/2)
    # Two halves of the list
    left = merge_sort(my_list[0:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    # merges lists
    return merge(left, right)


# Merge is a helper functio that will combine two SORTED list
# Big O: The mergring of all the split lists is O(n); each while loop needs to loop through each of the elements
# Big O: Adding both the spliting and merging together results in Big O(n log n) for merge sort
def merge(list1, list2):
    combinded = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combinded.append(list1[i])
            i += 1
        else:
            combinded.append(list2[j])
            j += 1  
    while i < len(list1):
        combinded.append(list1[i])
        i += 1
    while j < len(list2):
        combinded.append(list2[j])
        j += 1
    return combinded

# Quick sort
# Big O: O(n log n)
# Big O: Worst case is where the data is already sorted => O(n^2)
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

def quick_sort_helper(my_list, left, right):
    if left < right:
        # Right bound is moved up one to ensure the pivot index is not inculded in subsequent calls
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        # Left bound is moved up one to ensure the pivot index is not inculded in subsequent calls
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

# Pivot: helper function that does two things. 1. order everything in between the pivot indices and 2. Return the pivot index
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        # Two things to do: move swap index up on and run pivot with i (up to, but not including)
        if my_list[pivot_index] > my_list[i]:
            swap_index += 1
            swap(my_list, swap_index, i)
    # Lastly, swap the pivot and swap_index 
    swap(my_list, pivot_index, swap_index)
    return swap_index

# Swap: helper function to pivot
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] =  my_list[index2]
    my_list[index2] = temp

test_list = [4, 2, 6, 5, 1, 3]
# print(bubble_sort(test_list))
# print(selection_sort(test_list))
# print(insertion_sort(test_list))
# print(merge_sort(test_list))
print(quick_sort(test_list))
# print(test_list)

# ============================================================#
        # Using bubble sort to sort a Linked List #
# ============================================================#
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def bubble_sort(self):
        if self.length < 2:
            return
        # sorted_until is used to indentify what has already been sorted_until
        # At first this is nothing, so it is set to None
        sorted_until = None
        # This will only terminate when the linked list is "sorted until" the second value
        # This means everything after, and including, the second value is sorted and thus the entire list is sorted
        while sorted_until != self.head.next:
            # Variable set to the head at each iteration.  
            # It will be used to traverse the list from the start of each outer loop iteration
            current = self.head
            # This is where the actual sorting happens. Iterates until just before it hits the sorted_until variable
            # In the first iteration it will reach the end of the LinkedList
            while sorted_until != current.next:
                # Get the adjacent node to compare values
                next_node = current.next
                if current.value > next_node.value:
                    # Larger value moves towards the end of the LL
                    current.value, next_node.value = next_node.value, current.value
                # Move the current value to the next node in the list
                current = current.next
            # move the "sorted_until" boundary condition
            sorted_until = current

    def selection_sort(self):
        if self.length < 2:
            return
        outer_current = self.head
        while outer_current.next is not None:
            smallest = outer_current
            inner_current = outer_current.next
            while inner_current is not None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next
            if smallest != outer_current:
                outer_current.value, smallest.value = smallest.value, outer_current.value        
            outer_current = outer_current.next

    # Merge two linked lists
    def merge(self, other_list):
        # Create a dummy node that will point to the head after the first iteration  
        dummy = Node(0)
        # Assign a pointer to move from the dummy to the next values in the LL
        current = dummy
        # create a pointer to the input list so we can traverse it
        other_head = other_list.head
        # The head of both lists will move.
        while self.head is not None and other_head is not None:
            # If the current head value of the self list is less than the input list head's value
            if self.head.value < other_head.value:
                # set the pointer "current"'s next attribute to the head of the self list 
                current.next = self.head
                # move the lists head to the next position
                self.head = self.head.next
            else:
                
                current.next = other_head
                other_head = other_head.next
            current = current.next
        # If the input list was the first list to be fully appended into the "self" LL, simply connect the remainder of the LL via the latest self.head
        if self.head is not None:
            current.next = self.head
        # If the "self" list was the first list to be fully appended, connect the remainder of input the LL via the latest other_list.head (other_head)
        # and reassign the tail to the tail of the other_list (other_list.tail)
        else:
            current.next = other_head
            self.tail = other_list.tail
        self.head = dummy.next
        self.length += other_list.length