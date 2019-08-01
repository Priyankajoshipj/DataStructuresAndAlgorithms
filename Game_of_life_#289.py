#Solution for LeetCode problem No. 289
# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Modifications done in-place
def gameOfLife(board):
	m=len(board)
	n=len(board[0])
	copy=[[board[i][j] for j in range(n)] for i in range(m) ]
	for i in range(m):
	    neighbours=[(1,0),(0,-1),(1,-1),(-1,-1),(1,1),(0,1),(-1,0),(-1,1)]

	    for j in range(n):
	        countones=0
	        for ne in neighbours:

	            r= i+ne[0]
	            c= j+ne[1]

	            if((r>=0 and r<m) and (c>=0 and c<n) and abs(copy[r][c])==1):
	                countones+=1
	        if (copy[i][j]==1 and (countones<2 or countones>3)):
	            board[i][j]=0
	        if(copy[i][j]==0 and countones==3):
	            board[i][j]=1
        
