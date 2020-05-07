'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

def happyNum(num):

    #cast as string
    num_str = str(num)
    tot = 0

    #iterate over the digits
    for digit in num_str:
        #calculate the square for each digit
        s = int(digit)**2
        tot += s
    
    print(tot)

    if tot == 1:
        return True

    happyNum(tot)

out = happyNum(19)
print(out)

