# LeetCode: 34 Find first and last position of element in sorted array
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Time complexity O(logn + k )  where is the number of times target appears 
# Leetcode [Accepted] beats 93.61%
def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = 0
        right = n-1
        if nums[left] == target and nums[right] == target:
            return [left,right]
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if nums[left] == target and nums[right] == target:
                    return [left,right]
                left = mid
                right = mid
                while nums[right] == target:
                    right+=1
                    if right >=n:
                        break
                while nums[left] == target:
                    left-=1
                    if left<0:
                        break
                return [left+1,right-1]
        return [-1,-1]