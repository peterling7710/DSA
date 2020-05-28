'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Note:

All given inputs are in lowercase letters a-z.

'''

def longestCommonPrefix(strs):
    i = 0
    limit = 2**31
    prefix = ""

    if len(strs) == 0:
        return ""

    for st in strs:
        if len(st) < limit:
            limit = len(st)

    while i < limit:
        j = strs[0][i]
        print(f"j {j}")

        for st in strs:
            k = st[i]
            print(f"k {k}")
            
            if j != k:
                return prefix


        prefix += st[i]
        i+=1

    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
#Output: "fl"

print(longestCommonPrefix(["dog","racecar","car"]))
#Output: ""
#Explanation: There is no common prefix among the input strings.