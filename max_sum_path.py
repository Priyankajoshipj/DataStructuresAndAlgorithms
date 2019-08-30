'''
Maximum Sum Path in Two Arrays
Given two sorted arrays such the arrays may have some common elements.
Find the sum of the maximum sum path to reach from beginning of any array to end of any of the two arrays.
We can switch from one array to another array only at common elements. 
Note that the common elements do not have to be at same indexes.
'''
# Recursive Dynammic Approach
def max_sum_path(nums1, nums2):
	common = set(nums1) and set(nums2)
	dp = {}
	arr = nums1

	def rec_checksum(arr1, arr2, i, index,dp):
		arr = arr1 if i == 1 else arr2
		pair = (arr[index], i)
		if pair in dp:
			return dp[pair]
		if index == len(arr) - 1:
			dp[pair] = arr[index]
			return arr[index]

		if arr[index] in common:
			maxSum =  arr[index] + max(rec_checksum(arr1, arr2, 1, index + 1,dp), rec_checksum(arr1, arr2, 2, index + 1,dp) )
			dp[pair] = maxSum
			return maxSum
		else:
			if (arr[index+1], i) in dp:
				maxSum = dp[(arr[index+1], i)] + arr[index]
				dp[pair] = maxSum
			else: maxSum = arr[index] + rec_checksum(arr1, arr2, i, index + 1,dp)
			return maxSum

	return max(rec_checksum(nums1, nums2, 1, 0,dp), rec_checksum(nums1, nums2, 2, 0,dp))

print(max_sum_path([1, 3, 7, 10, 2],[1, 2, 7, 11]))
print(max_sum_path([2, 3, 7, 10, 12 ],[1, 5, 7, 8]))
print(max_sum_path([2, 3, 7, 10, 12, 15, 30, 34],[1, 5, 7, 8, 10, 15, 16, 19]))