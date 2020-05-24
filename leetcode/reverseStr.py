'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

def revStr(s):
    i = 0
    n = len(s) - 1
    
    mid = (n) // 2 + 1

    while i < mid:
        print(f"{s[i]} swapped with {s[n-i]}")
        print(mid)
        s[i], s[n-i] = s[n-i], s[i]
        i+=1

    return s

print(revStr(["h","e","l","l","o"]))
#print(revStr(["H","a","n","n","a","h"]))
#print(revStr(["H","a","n","R","e","h"]))
#print(revStr(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]))

#["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
#['a', 'm', 'a', 'n', 'a', 'P', ' ', ':', 'l', 'a', 'n', 'a', 'c', ' ', 'a', ' ', ',', 'n', 'a', 'l', 'p', ' ', 'a', ' ', ',', 'n', 'a', 'm', ' ', 'A']