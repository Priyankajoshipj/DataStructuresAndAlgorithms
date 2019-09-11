# 51. N-Queens
# Backtracking problem - [Leetcode] Hard
class Solution: #[Accepted]
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return [[]]
        if n == 1:
            return ['Q']
        result = []
        placed = set()
        result = self.NQueens(0, 0, result, placed, n)
        res = []
        for r in result:
            p = []
            for i in range(n):
                s = ''
                for j in range(n):
                    if (i, j) in r:
                        s += 'Q'
                    else:
                        s += '.'
                p.append(s)
            res.append(p)
        return res

    def NQueens(self, r, c, result, placed, n):
        if len(placed) == n :
            result.append(list(placed))
            return result
        else:
            for i in range(n):
                if self.isValid(i, c, placed, n):
                    placed.add((i, c))
                    result = self.NQueens(i, c+1, result, placed, n)
                    placed.remove((i, c))
            return result

    def isValid(self, r, c, placed, n):
        if r < n and c < n:
            for pos in placed:
                if pos[0] == r or pos[1] == c or abs(pos[0] - r) ==  abs(pos[1] - c):
                    return False
            return True
        return False