'''
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

'''

ex1 = [2,2,1]
ex2 = [4,1,2,1,2]

def singleNumMem(arr):
    
    #Define dict of seen records
    seen = {}

    #Frequency Count
    for a in arr:

        # if seen before increment
        if a in seen:
            seen[a] += 1
        else:
            seen[a] = 1

    # Loop through dictionary and return if we've only seen once
    for key, val in seen.items():
        if val == 1:
            return key
    



print(singleNumMem(ex1))
print(singleNumMem(ex2))


def singleNumPoint(arr):
    #Return for memoryless sol
    return