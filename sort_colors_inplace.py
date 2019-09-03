'''
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
def Sort_Colors_inplace(nums):
	
	left = 0
	right = len(nums) - 1
	i = 0
	while(i <= right):
		if nums[i] == 0:
			nums[left], nums[i] = nums[i], nums[left]
			left += 1
			i += 1
		elif nums[i] == 2:
			nums[right], nums[i] = nums[i], nums[right]
			right -= 1	
		else:
			i += 1
nums = [1,2,0,0]
Sort_Colors_inplace(nums)
print(nums)		

nums = [2,0,2,1,1,0]
Sort_Colors_inplace(nums)
print(nums)		