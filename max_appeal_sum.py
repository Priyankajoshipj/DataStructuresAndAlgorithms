# Amazon | OA 2019 | Find Pair With Max Appeal Sum
# Appeal sum = A[i] + A[j] + abs(i-j)
# Array is not sorted

def max_appeal_sum(A):
	maxs = float('-inf')
	Pair = (-1,-1)

	left = 0
	right = len(A) - 1

	while (left <= right):
		apSum = A[left] + A[right] + (right-left)
		if apSum > maxs:
			maxs = apSum
			Pair = (left, right)
		if A[left] < A[right]:
			left += 1
		else:
			right -= 1

	return Pair

print(max_appeal_sum([1, 6, 1, 1, 1, 1, 7])) #output: (1, 6)
print(max_appeal_sum([1, 3, -1])) #output: (1, 1)
print(max_appeal_sum([6, 2, 7, 4, 4, 1, 6]) #output: (0, 6)