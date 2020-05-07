"""
Given two strings, write a method to decide if one is a permutation of the other
"""
base = "ABC"
egtrue = "BAC"
egfalse = "ABCD"
egfalse2 = "VAC"


def checkPerm(word1, word2):

    #Check if words are the same length
    if len(word1) != len(word2):
        return False

    chars1 = set(word1)
    chars2 = set(word2)

    if chars1 == chars2:
        return True
    
    return False
    
print(f"Answer A: {checkPerm(base, egtrue)}")
print(f"Answer B: {checkPerm(base, egfalse)}")
print(f"Answer C: {checkPerm(base, egfalse2)}")

