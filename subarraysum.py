# [1,2,1,3] sum = 3
# ways = 3
# target = 3, n
# pass1: left = 0, right = 0, ways = 0, subsum = 1

def subarraySum(arr, target):
	n = len(arr)
	if n == 0:
		return 1 if target == 0 else 0

	left = 0
	right = 0
	ways = 0
	subsum = 0
	while(left <= right):
		if left == right:
			ways =  ways + 1 if arr[left] == target

		subsum += arr[right]
		if subsum == target:
			way += 1
			left += 1
			right += 1
		elif subsum > target:
			subsum -= arr[left]
			left += 1

		else:
			right += 1

