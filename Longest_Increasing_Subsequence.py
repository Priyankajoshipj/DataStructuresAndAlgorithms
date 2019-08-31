'''
300. Longest Increasing Subsequence [Accepted]
Input: [10,9,2,5,3,7,101,18]
Output: [2,3,7,101] -> 4
'''
# Time Complexity O(n^2)
def lengthOfLIS(nums):
	res = []
    if not nums:
        return 0
    maxLIS = 1
    res.append(1)
    right = 1

    while(right < len(nums)):
        left = 0
        count = 0
        while(left < right):
            if nums[left] < nums[right]:
                count = max(count, res[left])
            left += 1
        res.append(count + 1)
        maxLIS = max(res[right], maxLIS)
        right += 1

    return maxLIS

# Time complexity O(nlogn)

def lengthOfLIS(nums):