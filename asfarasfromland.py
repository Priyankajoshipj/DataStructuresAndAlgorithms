# 1162. As Far from Land as Possible
# Approach1 : DP table
from collections import deque
class Solution: # [Time limit Exceeded] O(n^2) 
    def maxDistance(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len( grid[0])
        
        queue = deque()
        
        if R == C and R == 1:
            return -1
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    queue.append((i, j))
        maxd = float('-inf')
        seen = set()
        dp = [[float('inf') for i in range(R)] for j in range(C)]
        neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            if grid[r][c] == 1:
                dp[r][c] = 0
            seen.add((r, c))
            
            for n in neigh:
                newR = r + n[0]
                newC = c + n[1]
                pair = (newR, newC)
                
                if newR > -1 and newR < R and newC > -1 and newC < C:
                    if grid[r][c] != 1:
                        dp[r][c] = min(dp[r][c], dp[newR][newC] + 1)
                    if pair not in seen and pair not in queue:
                        queue.append(pair)
                    
            
            maxd = max(maxd, dp[r][c])
        if maxd == float('-inf') or maxd == 0:
            maxd = -1 
        return maxd
# O(n^2) [Accepted]
# Approach 2: Grid Mutation, Removed extra time and space to generate and store DP grid
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len( grid[0])
        
        queue = deque()
        seen = set()
        if R == C and R == 1:
            return -1
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
       
        neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not queue or len(queue) == R*C:
            return -1
    
        while queue:
            r, c = queue.popleft()
            d = grid[r][c]
            for n in neigh:
                newR = r + n[0]
                newC = c + n[1]
                pair = (newR, newC)
                
                if newR > -1 and newR < R and newC > -1 and newC < C and grid[newR][newC] == -1 :
                    
                    grid[newR][newC] = d + 1
                    
                    queue.append((newR, newC))
                    
        return d