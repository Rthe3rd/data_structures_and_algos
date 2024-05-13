# Remove Duplicates
# You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.
# You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.
# Your function should not modify the original list, instead, it should create a new list with unique values and return it.
def remove_duplicates(my_list):
    check_set = set()
    unique  = []
    for element in my_list:
        if element not in check_set:
            unique.append(element)
            check_set.add(element)
    return unique

# Has Unique Chars
# Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.
# For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
def has_unique_chars(input):
    check_set = set()
    for letter in input:
        if not letter in check_set:
            check_set.add(letter)
        else:
            return False
    return True

# Longest Consecutive Sequence
# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
# Use sets to optimize the runtime of your solution.
# Input: An unsorted array of integers, nums.
# Output: An integer representing the length of the longest consecutive sequence in nums.
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        # This checks whether or not the number you are currently at is the start of the consecutive sequence. 
        # if there is a value one less, skip the current value
        if num - 1 not in num_set:
            # initialize the current number pointer
            current_num = num
            # initialize the current sequence length
            current_sequence = 1
            # continously peform checks for the next number in the potential sequence by checking for the current number plus 1 
            while current_num + 1 in num_set:
                # if the set contains the next number in the sequence, move your pointer up and add to the current sequence length
                current_num += 1
                current_sequence += 1
            # at the end, assign the longest sequence to the max between the current sequence the current longest sequence 
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence