#Leet code 213. House Robber II [Accepted]
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if not nums :
        return 0
    if n == 2:
        return max(nums[0],nums[1])
    if n == 1:
        return nums[0]
    
    def rob_ring(nums,start,end):
        cash = [None for i in range(len(nums)-1)]
        cash[0] = nums[start]
        cash[1] = max(nums[start],nums[start+1])
        index = 2
        while(index  < len(cash)):
            cash[index]=max(nums[index+start]+cash[index-2],cash[index-1])
            index+=1
        return cash[-1]
    return max(rob_ring(nums,0,n-1), rob_ring(nums,1,n))