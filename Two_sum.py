# Two Sum three variations:
# Sum of nums adding upto extactly target, if multiple pairs choose the one having higher values
# time and space: O(n)
def two_sum(nums, target):
	complementMap = {}

	pairs = []

	for i in range(len(nums)):
		complement = target - nums[i] 
		if nums[i] in complementMap:
			pairs.append([complementMap[nums[i]], i])
		complementMap[complement] = i
	maxP = float('-inf')
	print("Pairs found: ", pairs)
	for pair in pairs:
		if pair[0] > maxP:
			ans = pair
			maxp = pair[0]
		elif pair[1] > maxP:
			ans = pair
			maxp = pair[1]
	print("Greatest value pair: ")
	return ans

nums = [1, 2, 7, 8, 15]


print(two_sum(nums, 9))
# Leetcode 167. Two Sum II - Input array is sorted
#If array is sorted, return the max, pair :
# since the array is sorted we don't need to compare multiple pairs since the right pointer will be the highest always
# worst case : time - >o(n) space -> O(1)
def twoSum(self, numbers, target): #[Accepted]
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(numbers)
    left = 0 
    right = n-1
    
    while(left<right):
        pair_sum = numbers[left] + numbers[right]
        if pair_sum == target:
            return [left+1, right+1]
        elif pair_sum < target:
            left += 1
        else:
            right -= 1

# 653. Two Sum IV - Input is a BST
# Leetcode [Accepted]
def findTarget(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    def inorder(root, List):
        if not root:
            return 
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            List.append(root.val)
            root = root.right
        return List
    sorted_list = inorder(root, [])
    n = len(sorted_list)
    left = 0
    right = n - 1
    while (left < right):
        psum = sorted_list[left] + sorted_list[right]
        if psum == k:
            return True
        elif psum < k:
            left += 1
        else:
            right -= 1
    return False