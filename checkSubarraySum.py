class Solution: #[TLE]
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    	
        n = len(nums)
        if n < 2:
            return False
        if k == 1:
            return True
        maps = {}
        for i in range(n):
            maps[(i,i)] = nums[i]

        for j in range(n-1, -1, -1):
            for i in range(j-1, -1, -1):
                maps[(i, j)] = maps[(i, i)] +maps[(i+1, j)]
                if k == 0:
                    if maps[(i, j)] == 0:
                        return True
                else:
                    if maps[(i, j)] % k == 0:
                        return True
        return False
