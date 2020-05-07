'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''

grid = [[1,3,1],[1,5,1],[4,2,1]]

def minPathSum(grid):

    #Initialize starting point and dimensions of input matrix
    x = len(grid) - 1 
    y = len(grid[0]) - 1
    start = (0,0)
    globSum = float("inf")

    def traverse(pos, locSum):

        nonlocal globSum, x, y
        
        #If we are out of range of our matrix, then return
        if pos[0] > x or pos[1] > y:
            return
        
        #If we hit the bottom right, stop update globsum at that point
        if pos == (x,y):
            locSum += grid[x][y]
            if locSum < globSum:
                globSum = locSum
        
        #Traverse to the right
        traverse((pos[0] + 1, pos[1]), locSum + grid[pos[0]][pos[1]])

        #Traverse downwards
        traverse((pos[0], pos[1] + 1), locSum + grid[pos[0]][pos[1]])


    #Call our recursive helper function
    traverse(start, 0)

    #Return shortest path
    return globSum

#Out should be 7
print(minPathSum(grid))