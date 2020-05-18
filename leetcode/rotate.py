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
    n = len(nums)
    #Account for full rotations
    k %= n

    start = count = 0

    while count < n:

        current, prev = start, nums[start]
        
        while True:
            next_ind = (current + k) % n 
            print(f"next: {next_ind}")
            nums[next_ind], prev = prev, nums[next_ind]
            current = next_ind
            count += 1

            if start == current:
                break
        

        start += 1    
        print(f"start: {start}")

    return nums

#print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))

#Output: [5,6,7,1,2,3,4]
#Output: [3,99,-1,-100]
