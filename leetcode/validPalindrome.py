'''
 Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters 
and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

'''

def isPalindrome(s):

    if s == "":
        return True

    i=0
    j = len(s) - 1
    mid = len(s)//2 + 1
    print(mid)

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    ascii_alphanum = ascii_lowercase + ascii_uppercase + digits

    while i < mid:
        if s[i] not in ascii_alphanum:
            i+=1
            continue
        elif s[j] not in ascii_alphanum:
            j-=1
            continue
        if s[i].lower() != s[j].lower():
            return False

        i+=1
        j-=1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
#Output: true
print(isPalindrome("race a car"))
#Output: false