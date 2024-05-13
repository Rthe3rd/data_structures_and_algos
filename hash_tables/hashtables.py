# HashTables

# Big O:
    # The has operation is required for both set and get.  The hash method has a time complexity of O(1)
    # The worst case scenario for the big O for is O(n) -> all items are entered at the same "address" and you have to look at every item
    # In practice, the hasing functions in a langauge like python help this speed greatly by distributing keys over a 
    # large address space and get/set operations are considered O(1)   

class HashTable:
    def __init__(self, size = 7):
        # create an odd-lengthed array to be the "addresses"
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        # makes sure the the list at the given address doesn't already have a list in it to store key value pairs 
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        # return self.data_map[index][1]

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        # data_maps_at_index = self.data_map[index]
        for data_maps_at_index in self.data_map[index]:
            if key in data_maps_at_index:
                return data_maps_at_index[-1]

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for data_mapas_at_index in self.data_map[i]:
                    all_keys.append(data_mapas_at_index[0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ':', val)
    
    # Find if there is an item in both lists
    def item_in_common(self, list1, list2):
        test_hash = {}
        for item in list1: 
            # if item not in test_hash: -> not needed
            test_hash[item] = True
        for item in list2:
            if item in test_hash:
                return True
        return None
    
def find_duplicates(input_array):
    hash_table = {}
    dupes = []
    for item in input_array:
        if not hash_table.get(item):
            hash_table[item] = True
        elif item not in dupes:
            dupes.append(item)
    return dupes

def find_first_non_repeat(input_array):
    hash_table = {}
    for char in input_array:
        hash_table[char] = hash_table.get(char, 0) + 1
    for char in input_array:
        if hash_table[char] == 1:
            return char
    return None

#  Time Complexity: O(n * k log k) 
    # -> n: time to loop through the nunber of elements in the list
    # -> k log k:  sorting each string in the array, where k is the longest possible length of string
def group_anagrams(array_of_anagrams):
    all_anagrams = []
    anagrams_dict = {}
    for anagram in array_of_anagrams:
        if not "".join(sorted(anagram)) in anagrams_dict:
            anagrams_dict["".join(sorted(anagram))] = [anagram]
        else:
            anagrams_dict["".join(sorted(anagram))] = [*anagrams_dict["".join(sorted(anagram))], anagram]
    for key,value in anagrams_dict.items():
        all_anagrams.append(value)
    return all_anagrams

def two_sum(input_array, target):
    hash_table = {}
    indices = []
    for index in range(len(input_array)):
        compliment = target - input_array[index]
        if compliment in hash_table:
            return [hash_table[compliment], index]
        else:
            hash_table[input_array[index]] = index
    return []

def subarray_sum(nums, target):
    # hash_table that holds sum/index key/value pairs 
    # The running sum is never reset.  
    # If at any point the difference between your current sum and a previous sum, which is store in the hash_table as sum/index and
        # you check by using "current_sum - target in", is equal to your target, then there exists a consecutive sub-sum
    # Handling the Target in the List:
        # If the first number in nums is the target, current_sum - target would be 0. This 0 is already in our dictionary, allowing us to find the target right away.
    # Serving as a Placeholder for Logic:
        # This initial setup simplifies the for-loop code by providing a common starting point for summing and comparing.
    sum_index = {0: -1}
    current_sum = 0
    # iterate through i (index of the array) and num (the value of the array at that point)
    for i, num in enumerate(nums):
        # calculate the current sum
        current_sum += num
        # if the current_sum less the target value is in the sum/index hash
        # curent_sum - target -> this tells you whether or not the value you are currently at sums to the target
            # if so, return the value from the hash_map, + 1, that is held at the [current_sum - target] key
            # if not, put the index at the current sum 
        if current_sum - target in sum_index:
            print(sum_index)
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []

my_hashtable = HashTable()
my_hashtable.set_item('first', 100)
my_hashtable.set_item('another', 500)
my_hashtable.set_item('another 2', 800)
my_hashtable.set_item('third !', 200)
# my_hashtable.print_table()
# print(my_hashtable.item_in_common([7,2,3,4], [7,6,5,1]))
# print(find_duplicates(['1','2','1','3', '1', '3']))
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  

nums = [0, 1, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )