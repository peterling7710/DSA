'''
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle.
'''
import math

def check_sum(n, arr, i, j):
    s = sum(arr[i:j+1])
    print(f"sum of {arr[i]} and {arr[j]}")

    if s > n:
        n = s

    return n


def maxSubArr(nums):

    if len(nums) < 1:
        return 0
    
    local_max = nums[0]

    absolute_max = nums[0]

    for i in range(1, len(nums)):
        local_max = max([local_max + nums[i] , nums[i]])
        #print(f"local max: {local_max}")


        absolute_max = max([local_max, absolute_max])
        #print(f"absolute max: {absolute_max}")
    
    return absolute_max

print(maxSubArr([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArr([1,-1]))
print(maxSubArr([-1,1]))
print(maxSubArr([-2,-3,-1]))

