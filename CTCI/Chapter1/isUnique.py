"""
a) Determine if string has all unique characters
b) Do it without additional data structures
"""

unique = "this"
not_unique = "Failed Test"

def isUnique(word):
    #Time complexity: O(N)

    #Dictionary to store seen characters
    seen_chars = {}

    #Loop through characters of word
    for char in word:
        #If seen before return True
        if char in seen_chars.keys():
            return True
        #If not, add it to dictionary
        else:
            seen_chars[char] = True

    return False


def isUniqueLean(word):
    #Time complexity: O(N^2)

    for i in range (len(word)):
        for j in range (i + 1, len(word)):
            if word[i] == word[j]:
                return True

    return False




print(f"Answer A: {unique} is {isUnique(unique)}")
print(f"Answer A: {not_unique} is {isUnique(not_unique)}")

print(f"Answer B: {unique} is {isUniqueLean(unique)}")
print(f"Answer B: {not_unique} is {isUniqueLean(not_unique)}")

