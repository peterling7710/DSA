'''
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

def reverse(x):

    word = str(x)
    negative = False

    if word[0] == "-":
        negative = True
        word = word[1:]
    
    word = word[::-1]

    if negative:
        word = "-" + word
    
    if int(word) > (2**(31) - 1) or int(word) < (-2)**(31):
        return 0
    else:
        return int(word)


print(reverse(123))
#Output: 321
print(reverse(-123))
#Output: -321
print(reverse(120))
#Output: 21