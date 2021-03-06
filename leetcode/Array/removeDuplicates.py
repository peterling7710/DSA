'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and 
return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified 
to 0, 1, 2, 3, and 4 respectively.

'''

def removeDuplicates(nums):

    #Pointer to run through length of array
    i = 0

    #Pointer to replace values
    j = 1

    while i < len(nums) - 1:
        if nums[i]<nums[i+1]:
            nums[j] = nums[i+1]
            print(f"j is {j}")
            j+=1

        print(f"i is {i}")

        i+=1

    return nums[:j]


print(removeDuplicates([1,1,2]))
#print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
