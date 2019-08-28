class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def squaresList(n):
            squares = []
            i = 1
            pair = 1
            while pair <= n:
                squares.append(pair)
                i +=1
                pair = i * i
            return squares

        def rec_sq(dp, n, squares):
            if n in dp:
                return dp[n]
            if n in squares:
                dp[n] = 1
                return 1
            if squares == [1]:
                dp[n] = n
                return n

            mint = float('inf')
            for sq in squares:
                if sq > n:
                    break
                l = n - sq
                if l in dp:
                    rec  = 1 + dp[l]
                else:
                    rec = rec_sq(dp, l, squares) + 1
                mint = min(mint, rec)
                dp[n] = mint
            return dp[n]

        return rec_sq({}, n, squaresList(n))