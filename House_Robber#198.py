# House Robber #198. leetcode [Accepted]
def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    cash = [None for i in range(n)]
    cash[0] = nums[0]
    cash[1] = max(nums[1],nums[0])
    index = 2
    while( index <n):
        cash[index]=max(nums[index]+cash[index-2],cash[index-1])
        index+=1
   
    return cash[-1]
