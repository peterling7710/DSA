'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

'''

def moveZeroes(nums):
    count = 0
    inds = []

    for ind, val in enumerate(nums):
        if val == 0:
            inds.append(ind)
            count += 1

    for ind in sorted(inds, reverse=True):
        del nums[ind]

    nums +=  count * [0] 

    return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,0,1]))