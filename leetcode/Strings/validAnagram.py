'''
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''

def isAnagram(s, t):

    #If the length is the same and the amount of characters if the same -> return True
    #take frequency count of both and compare dictionaries
    freq_s = {}
    freq_t = {}

    if len(s) != len(t):
        return False

    for char in s:
        if char in freq_s:
            freq_s[char] +=1
        else:
            freq_s[char]=1
    
    for char in t:
        if char in freq_t:
            freq_t[char] +=1
        else:
            freq_t[char]=1

    if freq_s != freq_t:
        return False

    return True





print(isAnagram(s = "anagram", t = "nagaram"))
#Output: true

print(isAnagram(s = "rat", t = "car"))
#Output: false