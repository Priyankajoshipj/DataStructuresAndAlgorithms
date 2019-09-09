# 494. Target Sum [Accepted]
# Add a plus or minus sign to each element and count the total number of sign assignment to sum up to a given target
def findTargetSumWays(nums, target):
	n = len(nums)
	if n == 0:
		return 0
	if n == 1:
		return 0 if nums[0] != abs(target) else 1
	def helper(num, sumt):
		if not num:
			return 0 if sumt != target else 1
		nu = num[0]

		return helper(num[1:], sumt + nu) + helper(num[1:], sumt - nu)

	return helper(nums, 0)

print(findTargetSumWays([1, 1, 1, 1, 1], 3))

def findTargetSumWaysDP(nums, target):
	n = len(nums)
	if n == 0:
		return 0
	if n == 1:
		return 0 if nums[0] != abs(target) else 1
	def helper(i, sumt, dp):
		if i >= n:
			return 0 if sumt != target else 1
		nu = nums[i]
		if (i, sumt) not in dp:
			dp[(i, sumt)] = helper(i + 1, sumt + nu, dp) + helper(i + 1, sumt - nu, dp)
		
		return dp[(i, sumt)]

	return helper(0, 0, {})

print(findTargetSumWaysDP([1, 1, 1, 1, 1], 3))