def plusOne(digits):

    n = len(digits) - 1

    if digits[0] == 0:
        return [1]
    
    if digits[n] != 9:
        digits[n]+=1
        return digits
    else:
        i = n

        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

            i -= 1

    if digits[0] == 0:
        digits.insert(0, 1)
    return digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([7,9,9,9]))
print(plusOne([9,9,9,9]))
print(plusOne([6,3,9,9]))

