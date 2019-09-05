# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell. # Leetcode-> 542. 01 Matrix
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        out = [[float('inf') for c in cols] for r in rows]
        seen = set()
        
        neighbours = [(-1,0),(0,-1),(1,0),(0,1)]
        queue = deque()

        queue.append((0, 0, 0))

        while queue:
        	r, c, distance = queue.popleft()

        	if nums[r][c] == 0:
        		out[r][c] = 0
        	else:
        		





