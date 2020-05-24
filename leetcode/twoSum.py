'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

def twoSum(nums, target):
    
    seen = {}

    #Frequency count
    for ind, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], ind]
        else:
            seen[num] = ind
        
print(twoSum(nums = [2, 7, 11, 15], target = 9))
print(twoSum(nums = [2, 7, 11, 15], target = 18))
print(twoSum(nums = [2, 7, 11, 15], target = 22))

print(twoSum([3,2,4], 6))
