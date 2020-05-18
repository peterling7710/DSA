'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 2 * 10^4
    It's guaranteed that nums[i] fits in a 32 bit-signed integer.
    k >= 0


'''
def rotate(nums, k):

    i = 0
    count = 0
    temp = None

    while count < len(nums):
        
        #Calculate new position with rotation
        ind = i + k

        #Check if at the end of the array
        if ind >= len(nums):
            ind -= len(nums)
        
        temp = nums[ind]
        curr = nums[i]

        if nums[ind] == nums[i]:
            
        # SWAP 
        nums[ind] = curr
        nums[ind] = nums[i]

        i = ind

        count += 1

    return nums    

print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))

#Output: [5,6,7,1,2,3,4]
#Output: [3,99,-1,-100]
