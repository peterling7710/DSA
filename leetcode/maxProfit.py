'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

def maxProfit(prices) -> int:

    if len(prices) <= 1: 
        return 0

    back=mprof=0
    front = 1

    while front < len(prices):
    
        #If decreasing
        if prices[front] < prices[back]:
            back = front

        prof = prices[front]-prices[back]

        if prof > mprof:
            mprof = prof
        front+=1

    return mprof

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1,2]))

