"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product 
fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are 
also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be 
bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first 
bad version. You should minimize the number of calls to the API.

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 


"""
def isBadVersion(n):

    return bool(n)

def firstBadVersion(self, n):

        # If no memory constraints
        a = [i for i in range (n + 1)]

        def traverse(arr):
            nonlocal a
            
            mid = len(arr) // 2

            if isBadVersion(arr[mid]) == True and isBadVersion(arr[mid-1]) == False:
                print("Got here 1")
                return arr[mid]
            
            if isBadVersion(arr[mid]) == True and len(arr) == 1:
                print("Got here 2")
                return arr[mid]

            if isBadVersion(arr[mid]) == False:
                traverse(arr[mid+1:])

            if isBadVersion(arr[mid]) == True:
                traverse(arr[:mid])
            
        out = traverse(a)

        return out
    
