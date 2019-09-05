# The complexity will be O(m∗n∗4s) where m is the no. of rows and n is the no. of columns 
# in the board and s is the length of the input string.
# 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        R = len(board)
        C = len(board[0])
        if (R==C and R==1):
            return board[0][0] == word
        seen = set()
        
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y, word):          
            if not word:
                return True
            res = False
            seen.add((x, y))
            for n in neighbours:
                r = x + n[0]
                c = y + n[1]
                if r > -1 and r < R and c > -1 and c < C and (r, c) not in seen and board[r][c] == word[0]:
                    res = res or dfs(r, c, word[1:])
            seen.remove((x, y))
            return res
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and dfs(i, j, word[1:]):
                    return True
        return False