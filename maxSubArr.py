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

def maxSubArr(nums):
    i = 0
    j = 0

    largest = sum(nums[i:j+1])

    while j >= i and j < len(nums) and i < len(nums):
        print(i,j)

        last = sum(nums[i:j])
        current = sum(nums[i:j+1])

        if current > largest:
            largest = current
        
        if current < last or j == len(nums) - 1:
            while i <= j:
                print(i,j)

                last = sum(nums[i-1:j+1])
                current = sum(nums[i:j+1])

                if current > largest:
                    largest = current

                if current > last:
                    break

                i += 1

        j+=1
    
    return largest

out = maxSubArr([-2,1,-3,4,-1,2,1,-5,4])
print(out)

