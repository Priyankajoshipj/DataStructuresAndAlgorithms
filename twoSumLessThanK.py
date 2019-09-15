'''
1099. Two Sum Less Than K [Leetcode Premium]
Given an array A of integers and integer K, return the maximum S 
such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.
Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
'''
def twoSumLessThanK(A, K):
	if not A:
        return -1
    n = len(A)
    maxp = float('-inf')
    A.sort()
    left, right = 0, n - 1

    while left < right:
        sump = A[left] + A[right]
        if  sump < K:
            maxp = max(maxp, sump)
            left += 1
        else:
            right -= 1
    return maxp if maxp != float('-inf') else -1

A = [10,20,30]
K = 15

print(twoSumLessThanK(A, K))
A = [34,23,1,24,75,33,54,8]
K = 60
print(twoSumLessThanK(A, K))