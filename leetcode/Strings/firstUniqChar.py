'''
First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

'''

def firstUniqChar(s):
    
    seen = {}

    #frequency count
    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for key, value in seen.items():
        print(key,value)
        if value == 1:
            return s.index(key)
    
    return -1

print(firstUniqChar("leetcode"))
#return 0.

print(firstUniqChar("loveleetcode"))
#return 2.

