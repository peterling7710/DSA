def arrInt(nums1, nums2):

    seen = {}
    out = []

    #Frequency count of first arr
    #O(nm)
    for num in nums1:
        if num in seen:
            seen[num] += 1
        else: 
            seen[num] = 1

    #If we've seen that number before in 1, we push it to output arr 
    for num in nums2:
        if num in seen and seen[num] > 0:
            out.append(num)
            seen[num] -= 1

    return out
    

print(arrInt([4,9,5], [9,4,9,8,4]))
print(arrInt(nums1 = [1,2,2,1], nums2 = [2,2]))
#Output: [4,9]

#Output: [2,2]

