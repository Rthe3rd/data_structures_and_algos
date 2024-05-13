
def subset(nums):
    subset_holder = []

    subset = []

    def __r_subset(i):
        if i >= len(nums):
            print("ADDING A SUBSET:" , subset)
            subset_holder.append(subset.copy())
            print("Here are all the current subsets:" , subset_holder)
            print("============")
            return
        subset.append(nums[i])
        __r_subset(i + 1)

        subset.pop()
        __r_subset(i + 1)

    __r_subset(0)
    return subset_holder


nums = [1,2,3]

print(subset(nums))