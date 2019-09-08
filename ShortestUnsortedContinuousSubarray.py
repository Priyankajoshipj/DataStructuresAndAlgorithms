# 581. Shortest Unsorted Continuous Subarray
'''
input: [2, 6, 4, 8, 10, 9, 15]
output = 5
brute force O(n^3) check for all sub arrays possible
better brute force O(n^2)
'''
def ShortestUnsortedContSubarray(nums):
	n = len(nums)
	left = n - 1
	right = 0
	for i in range(n):
		for j in range(i + 1, n):
			if nums[i] > nums[j]:
				left = min(left, nums[i])
				right = max(right, nums[j])

	return 0 if right - left < 0 else right - left + 1

# better approach O(n) using stack and two pass

def ShortestUnsortedContSubarray1(nums):
	n = len(nums)
	stack = [0]
	left = n - 1
	# get min from the right
	for i in range(n):
		while stack and nums[stack[-1]] > nums[i]:	
			left = min(left, stack.pop())
		stack.append(i)
	
	# Get max from the right
	stack = [n - 1]
	for i in range(n):
		while stack and nums[stack[-1]] < nums[i]:
			
			right = max(left, stack.pop())
		stack.append(i)

	return 0 if right - left < 0 else right - left + 1


v = [2, 6, 4, 8, 10, 9, 15]
print("Approach1 ", ShortestUnsortedContSubarray(v))


print("Approach2 ", ShortestUnsortedContSubarray1(v))