'''

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().

'''

def strStr(haystack, needle):
    i = 0
    n = len(needle)

    if needle == "":
        return 0

    while i < len(haystack) - n + 1:
        if haystack[i:i+n] == needle:
            return i

        i+=1
        
    return -1

print(strStr(haystack = "hello", needle = "ll"))
#Output: 2

print(strStr(haystack = "aaaaa", needle = "bba"))
#Output: -1

print(strStr("a", "a"))
# 0 