class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
def constructMaxBinaryTree(nums):
	return construct(nums, 0, len(nums))

def construct(nums, l, r):
	if l == r:
		return None

	maxi = findMaxIndex(nums, l, r)
	root = TreeNode(nums[maxi])

	root.left = construct(nums, l, maxi)
	root.right = construct(nums, maxi + 1, r)

	return root

def findMaxIndex(nums, l, r):
	maxn = l
	for i in range(l, r):
		maxn = i if nums[i] > nums[maxn] else maxn

	return maxn

def inorder(root, out):
	if not root:
		return out
	out = inorder(root.left, out)
	out.append(root.val)
	out = inorder(root.right, out)

	return out

nums = [3,2,1,6,0,5]
root = constructMaxBinaryTree(nums)

out = inorder(root, [])
print(out)